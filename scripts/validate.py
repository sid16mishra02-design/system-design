"""Check source preservation, topic budgets, curriculum coverage, and links."""
from pathlib import Path
import hashlib
import json
import os
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
linkmap = json.loads((ROOT/'metadata/inline-link-map.json').read_text(encoding='utf-8'))
comparisons = json.loads((ROOT/'metadata/tradeoffs.json').read_text(encoding='utf-8'))
tradeoff_page = (ROOT/'practice/TRADEOFFS.md').read_text(encoding='utf-8')
for row in comparisons:
    check(row['words'] == words(' '.join([row['comparison'], row['choice'], row['example']])),
          f'Tradeoff count mismatch: {row["comparison"]}')
    check(f'| {row["comparison"]} | {row["choice"]} | {row["example"]} |' in tradeoff_page,
          f'Local tradeoff explanation missing: {row["comparison"]}')


def localize_course_links(text, path):
    def relocate(match):
        url, separator, fragment = match[0].partition('#')
        target = os.path.relpath(ROOT/linkmap[url], (ROOT/path).parent).replace('\\', '/')
        return target + (separator + fragment if separator else '')
    return re.sub(r'(?<=\]\()https://karanpratapsingh.com/courses/system-design(?:/[a-z0-9-]+)?(?:#[a-z0-9-]+)?(?=\))', relocate, text)


audit = json.loads((ROOT/'metadata/content-audit.json').read_text(encoding='utf-8'))
for entry in audit:
    text = (ROOT/entry['companion_path']).read_text(encoding='utf-8')
    excerpt = re.search(r'<!-- BEGIN ORIGINAL TOPIC -->\n(.*?)\n<!-- END ORIGINAL TOPIC -->', text, re.S)
    check(excerpt is not None, f'Missing inline lesson: {entry["topic"]}')
    if excerpt:
        check(excerpt[1] == localize_course_links(original[entry['topic']].rstrip(), entry['companion_path']),
              f'Copied original text changed: {entry["topic"]}')
    if entry.get('measurement') == 'full_companion':
        added = words(text.split('## Complete lesson')[0])
    else:
        example = re.search(r'## Make it concrete\n\n(.*?)\n\n\[Next topic', text, re.S)
        checkpoint = re.search(r'## Before moving on\n\n(.*?)\n\n\[Next topic', text, re.S)
        added = words(example[1]) if example else words(checkpoint[1]) if checkpoint else 0
    check(entry['inline_teaching_words'] == added, f'Inline count mismatch: {entry["topic"]}')
    extra = sum(row['words'] for row in comparisons if row['topic'] == entry['topic'])
    check(entry['tradeoff_teaching_words'] == extra, f'Tradeoff allocation mismatch: {entry["topic"]}')
    added += extra
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
    target = entry['path']
    check(target is not None and (ROOT/target).is_file(), f'No local lesson: {entry["title"]}')
    check(not entry['resource_only'], f'Core topic still requires external reading: {entry["title"]}')
    check(schedule.count(f'[{entry["title"]}]({target})') == 1,
          f'Topic must be scheduled once: {entry["title"]}')

new_lessons = json.loads((ROOT/'metadata/original-lessons.json').read_text(encoding='utf-8'))
check(len(new_lessons) == 20, 'Expected twenty original lessons under the approved exception')
for entry in new_lessons:
    text = (ROOT/entry['path']).read_text(encoding='utf-8')
    teaching = text.split('## Optional further reading')[0].split('\n\n', 2)[2].rstrip()
    check(words(teaching) == entry['words'], f'Original lesson word count mismatch: {entry["topic"]}')
    check('## Optional further reading' in text, f'Unmarked external references: {entry["topic"]}')

# Source archives can remain for provenance, but are not required reading.
for entry in topics:
    text = (ROOT/entry['path']).read_text(encoding='utf-8')
    check(not re.search(r'\]\([^)]*sources/(?:karan|ashish)/README\.md', text),
          f'Lesson sends reader to an archive: {entry["title"]}')
    check(not re.search(r'\]\(https://karanpratapsingh.com/courses/system-design', text),
          f'Lesson sends reader to the original course: {entry["title"]}')
check('**Read first**' not in schedule, 'Schedule retains the old source-detour instructions')

# Check authored Markdown only. Original source links are deliberately preserved;
# any pre-existing problems are source issues rather than edited silently here.
link_count = 0
for p in ROOT.rglob('*.md'):
    if 'sources' in p.relative_to(ROOT).parts:
        continue
    text = p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
        target = target.strip('<>')
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
print(f'PASS: {len(manifest["files"])} unchanged source files; {len(audit)} verbatim inline readings and topic budgets; '
      f'{len(new_lessons)} original lessons; {len(topics)} local scheduled concepts; 154 daily rows; {link_count} local links.')
print('External resource access is not guaranteed; original source links are preserved.')
