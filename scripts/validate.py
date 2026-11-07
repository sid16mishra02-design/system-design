"""Check source preservation, disclosed teaching counts, inquiry coverage, and links."""
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
    check(row['words'] == words(' '.join([row['comparison'], row['choice'], row['example'], row['opening_question']])),
          f'Tradeoff count mismatch: {row["comparison"]}')
    check(row['opening_question'] in tradeoff_page and '?' in row['opening_question'],
          f'Missing comparison scenario: {row["comparison"]}')
    check(f'| {row["comparison"]} | {row["choice"]} | {row["example"]} |' in tradeoff_page,
          f'Local tradeoff explanation missing: {row["comparison"]}')


def localize_course_links(text, path):
    def relocate(match):
        url, separator, fragment = match[0].partition('#')
        target = os.path.relpath(ROOT/linkmap[url], (ROOT/path).parent).replace('\\', '/')
        return target + (separator + fragment if separator else '')
    text = re.sub(r'(?<=\]\()https://karanpratapsingh.com/courses/system-design(?:/[a-z0-9-]+)?(?:#[a-z0-9-]+)?(?=\))', relocate, text)
    image_base='https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/'
    def local_image(match):
        target=ROOT/'assets/source-diagrams'/match.group(0)[len(image_base):]
        return os.path.relpath(target,(ROOT/path).parent).replace('\\','/')
    return re.sub(re.escape(image_base)+r'[^)\s]+',local_image,text)


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
        inquiry = re.search(r'<!-- BEGIN INQUIRY -->\n## Try solving this first\n\n(.*?)\n<!-- END INQUIRY -->', text, re.S)
        added += words(inquiry[1]) if inquiry else 0
    check(entry['inline_teaching_words'] == added, f'Inline count mismatch: {entry["topic"]}')
    extra = sum(row['words'] for row in comparisons if row['topic'] == entry['topic'])
    check(entry['tradeoff_teaching_words'] == extra, f'Tradeoff allocation mismatch: {entry["topic"]}')
    added += extra
    baseline = words(original[entry['topic']])
    check(entry['original_words'] == baseline, f'Source count mismatch: {entry["topic"]}')
    check(entry['added_explanatory_words'] == added, f'Addition count mismatch: {entry["topic"]}')
    check(entry['exceeds_initial_30_percent'] == (added > int(.30*baseline)),
          f'Expansion disclosure mismatch: {entry["topic"]}')
    check(entry['addition_policy']=='Reader-approved clarity expansion; actual addition reported',
          f'Missing revised addition policy: {entry["topic"]}')
    check(entry['changed_original_words'] == 0, f'Source-edit audit mismatch: {entry["topic"]}')

topics = json.loads((ROOT/'metadata/topics.json').read_text(encoding='utf-8'))
localized_images=json.loads((ROOT/'metadata/localized-source-images.json').read_text(encoding='utf-8'))
check(len(localized_images)==len({x['source_url'] for x in localized_images}), 'Duplicate localized source image')
for image in localized_images:
    path=ROOT/image['path']
    check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==image['sha256'],
          f'Localized source image missing or changed: {image["path"]}')
for path in list((ROOT/'curriculum').rglob('*.md'))+list((ROOT/'practice').glob('*.md')):
    check('raw.githubusercontent.com/karanpratapsingh/portfolio/' not in path.read_text(encoding='utf-8'),
          f'Remote Karan image remains in reading path: {path.relative_to(ROOT)}')
inquiry_review = json.loads((ROOT/'metadata/inquiry-review.json').read_text(encoding='utf-8'))
check(len(inquiry_review)==71 and {x['topic'] for x in inquiry_review}=={x['title'] for x in topics},
      'Every foundational topic must have a reviewed opening problem')
for opening in inquiry_review:
    text=(ROOT/opening['path']).read_text(encoding='utf-8')
    check(opening['challenge'] in text and '?' in opening['challenge'], f'Missing inquiry: {opening["topic"]}')
    check(text.index('<!-- BEGIN INQUIRY -->')<text.index('<!-- END INQUIRY -->'),f'Invalid inquiry block: {opening["topic"]}')
    if '<!-- BEGIN ORIGINAL TOPIC -->' in text:
        check(text.index('<!-- END INQUIRY -->')<text.index('<!-- BEGIN ORIGINAL TOPIC -->'),
              f'Scenario follows the answer: {opening["topic"]}')
    check(opening['words']==words(opening['challenge']),f'Inquiry count mismatch: {opening["topic"]}')
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

depth_review = json.loads((ROOT/'metadata/depth-review.json').read_text(encoding='utf-8'))
expected_counts = {x['topic']: x['inline_teaching_words'] for x in audit}
expected_counts.update({x['topic']: x['words'] for x in new_lessons})
check(len(depth_review) == 77 and {x['topic'] for x in depth_review} == set(expected_counts),
      'Applied-depth review must cover every foundation and case/method lesson')
for entry in depth_review:
    check(entry['teaching_words_now'] == expected_counts.get(entry['topic']),
          f'Depth-review count mismatch: {entry["topic"]}')

# The editorial audit is backed by exact quotes within real heading sections.
topic_review = json.loads((ROOT/'metadata/topic-validation.json').read_text(encoding='utf-8'))
practice_review = json.loads((ROOT/'metadata/practice-validation.json').read_text(encoding='utf-8'))
animations = json.loads((ROOT/'metadata/animations.json').read_text(encoding='utf-8'))
animation_by_id = {x['id']: x for x in animations}
check(len(topic_review) == len(topics) and {x['topic'] for x in topic_review} == {x['title'] for x in topics},
      'Category/topic audit must cover each foundational topic exactly once')
expected_practice={x['comparison'] for x in comparisons} | cases | {'System Design Interviews'}
check(len(practice_review)==17 and {x['topic'] for x in practice_review}==expected_practice,
      'Practice audit must cover eleven comparisons, interview method, and five designs')
check(len({x['category'] for x in topic_review+practice_review})==13,'Expected coverage of all thirteen categories')


def evidence_section(text, anchor):
    headings=[]
    in_code=False
    used=set()
    offset=0
    for line in text.splitlines(keepends=True):
        if re.match(r'^\s*(```|~~~)', line):
            in_code=not in_code
        if not in_code:
            match=re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$',line)
            if match:
                label=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',match[2])
                base=re.sub(r'[^\w\- ]','',label.lower()).replace(' ','-')
                candidate=base
                number=0
                while candidate in used:
                    number+=1;candidate=f'{base}-{number}'
                used.add(candidate)
                headings.append((offset,len(match[1]),candidate))
        offset+=len(line)
    for i,(start,level,name) in enumerate(headings):
        if name==anchor:
            stop=next((p for p,depth,_ in headings[i+1:] if depth<=level),len(text))
            return text[start:stop]
    return ''


for entry in topic_review+practice_review:
    text=(ROOT/entry['path']).read_text(encoding='utf-8')
    for key in ['fundamental_evidence','application_evidence']:
        evidence=entry[key]
        section=evidence_section(text,evidence['anchor'].lstrip('#'))
        check(bool(section) and evidence['quote'] in section,
              f'{key} is not grounded at its heading: {entry["topic"]}')
    inquiry=entry['inquiry_evidence']
    check(inquiry['quote'] in evidence_section(text,inquiry['anchor'].lstrip('#')),
          f'Opening scenario is not grounded at its heading: {entry["topic"]}')
    check(bool(entry['problem_solved']) and bool(entry['design_scenario']) and len(entry['application_steps'])>=2,
          f'Incomplete application audit: {entry["topic"]}')
    check(not entry['needs_animation'] or bool(entry['animations']),f'Missing recommended animation: {entry["topic"]}')
    for key in entry['animations']:
        check(key in animation_by_id and entry['topic'] in animation_by_id[key]['topics'],
              f'Animation is not associated with this topic: {entry["topic"]}')
        if key in animation_by_id:
            target=os.path.relpath(ROOT/animation_by_id[key]['gif'],(ROOT/entry['path']).parent).replace('\\','/')
            # Main or related walkthrough is reachable from this lesson.
            check(target in text or f'animations/{key}.md' in text,f'Walkthrough not linked: {entry["topic"]}')

for entry in animations:
    for field,hash_field in [('gif','gif_sha256'),('static','static_sha256')]:
        path=ROOT/entry[field]
        check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==entry[hash_field],
              f'Animation asset missing or changed: {entry[field]}')
    check(entry['encoded_frame_count']>1 and entry['duration_ms']>0,f'Static file mislabeled as animation: {entry["id"]}')
    check(entry['caption_words']==sum(words(s['caption']) for s in entry['steps']),f'Caption accounting mismatch: {entry["id"]}')
    transcript=(ROOT/'animations'/f'{entry["id"]}.md').read_text(encoding='utf-8')
    check(all(s['caption'] in transcript for s in entry['steps']),f'Missing text alternative: {entry["id"]}')

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
print(f'PASS: {len(manifest["files"])} unchanged source files; {len(localized_images)} byte-verified local source images; '
      f'{len(audit)} verbatim inline readings and disclosed teaching counts; {len(new_lessons)} original lessons; '
      f'{len(topics)} local scheduled concepts; 154 daily rows; {link_count} local links.')
print(f'PASS: {len(topic_review)} topic + {len(practice_review)} practice/comparison evidence reviews across 13 categories; {len(animations)} animation/still/text sets.')
print('External resource access is not guaranteed; original source links are preserved.')
