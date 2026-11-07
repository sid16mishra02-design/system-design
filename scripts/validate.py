"""Check source preservation, topic budgets, curriculum coverage, and links."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


def words(text):
    return len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", text))


def sections(text):
    headers = list(re.finditer(r'^# (.+)$', text, re.M))
    return {m[1]: text[m.start():headers[i+1].start() if i+1 < len(headers) else len(text)]
            for i, m in enumerate(headers)}


def slugs(text):
    """GitHub heading IDs, including duplicate-heading suffixes."""
    used = set()
    result = set()
    in_code = False
    for line in text.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not m:
            continue
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', m[1])
        base = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        candidate = base
        suffix = 0
        while candidate in used:
            suffix += 1
            candidate = f'{base}-{suffix}'
        used.add(candidate)
        result.add(candidate)
    result.update(re.findall(r'<a\s+(?:name|id)=["\']([^"\']+)', text))
    return result


manifest = json.loads((ROOT/'metadata/sources.json').read_text(encoding='utf-8'))
for entry in manifest['files']:
    p = ROOT/entry['path']
    check(p.is_file(), f'Missing source file: {p}')
    if p.is_file():
        check(hashlib.sha256(p.read_bytes()).hexdigest() == entry['sha256'],
              f'Source was modified: {entry["path"]}')

original = sections((ROOT/'sources/karan/README.md').read_text(encoding='utf-8'))
audit = json.loads((ROOT/'metadata/content-audit.json').read_text(encoding='utf-8'))
for entry in audit:
    text = (ROOT/entry['companion_path']).read_text(encoding='utf-8')
    example = re.search(r'## Companion example\n\n(.*?)\n\n## Continue', text, re.S)
    added = words(text) if entry.get('measurement') == 'full_companion' else words(example[1]) if example else 0
    baseline = words(original[entry['topic']])
    check(entry['original_words'] == baseline, f'Source count mismatch: {entry["topic"]}')
    check(entry['added_explanatory_words'] == added, f'Addition count mismatch: {entry["topic"]}')
    check(added <= int(.30*baseline), f'30% addition limit exceeded: {entry["topic"]}')
    check(entry['changed_original_words'] == 0, f'Source-edit audit mismatch: {entry["topic"]}')

topics = json.loads((ROOT/'metadata/topics.json').read_text(encoding='utf-8'))
check(len({x['title'] for x in topics}) == len(topics), 'Duplicate scheduled topic')
cases = {'URL Shortener', 'WhatsApp', 'Twitter', 'Netflix', 'Uber'}
excluded = {'System Design', 'Table of contents', 'Next Steps', 'References', 'System Design Interviews'} | cases
check(set(original)-excluded == {x['topic'] for x in audit if x.get('measurement') != 'full_companion'}, 'An original concept is missing from the curriculum')
schedule = (ROOT/'SCHEDULE.md').read_text(encoding='utf-8')
check(len(re.findall(r'^### Week \d+$', schedule, re.M)) == 22, 'Expected 22 weeks')
check(len(re.findall(r'^\| ☐ \| [1-7] \|', schedule, re.M)) == 154, 'Expected seven days per week')
for entry in topics:
    target = entry['url'] if entry['resource_only'] else entry['path']
    check(schedule.count(f'[{entry["title"]}]({target})') == 1,
          f'Topic must be scheduled once: {entry["title"]}')

# Check authored Markdown only. Original source links are deliberately preserved;
# any pre-existing problems are source issues rather than edited silently here.
link_count = 0
for p in ROOT.rglob('*.md'):
    if 'sources' in p.relative_to(ROOT).parts:
        continue
    text = p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        if urlsplit(target).scheme:
            continue
        target = unquote(target)
        path, _, anchor = target.partition('#')
        dest = (p.parent/path).resolve() if path else p
        link_count += 1
        check(dest.exists(), f'Broken local link in {p.relative_to(ROOT)}: {target}')
        if dest.is_file() and anchor and dest.suffix == '.md':
            check(anchor in slugs(dest.read_text(encoding='utf-8')),
                  f'Missing heading in {p.relative_to(ROOT)}: {target}')

# The extracted problem list must retain all source labels and destinations.
ashish = (ROOT/'sources/ashish/README.md').read_text(encoding='utf-8')
source_bank = ashish[ashish.index('## 💻 System Design Interview Problems'):ashish.index('## 📇 Courses')]
bank = (ROOT/'practice/PROBLEMS.md').read_text(encoding='utf-8')
for link in re.findall(r'^- \[[^\]]+\]\([^\n]+\)', source_bank, re.M):
    check(link in bank, f'Original practice link missing: {link}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(manifest["files"])} unchanged source files; {len(audit)} topic budgets; '
      f'{len(topics)} scheduled concepts; 154 daily rows; {link_count} local links.')
print('External resource access is not guaranteed; original source links are preserved.')
