"""Decode all frames and verify four-second stages, infinite loops, and visible embeds."""
from pathlib import Path
from PIL import Image
import json
import re

root=Path(__file__).resolve().parents[1]
entries=json.loads((root/'metadata/animations.json').read_text(encoding='utf-8'))
stories=json.loads((root/'metadata/animation-stories.json').read_text(encoding='utf-8'))
assert {x['id'] for x in entries}=={x['id'] for x in stories}
for story in stories:
    ids={n['id'] for n in story['nodes']}
    assert len(ids)==len(story['nodes'])<=8,story['id']
    assert len({(n['col'],n['row']) for n in story['nodes']})==len(ids),story['id']
    assert all(0<=n['col']<=3 and 0<=n['row']<=1 for n in story['nodes']),story['id']
    assert all(e['from'] in ids and e['to'] in ids for e in story['links']),story['id']
    assert story['objective'] and story['scenario'] and story['tradeoff'],story['id']
    for step in story['steps']:
        assert set(step['updates'])<=ids,story['id']
        assert all(0<=i<len(story['links']) for i in step['active']),story['id']
        assert step['caption'] and step['insight'] and len(step['detail'])>=2,story['id']
for item in entries:
    assert item['step_duration_ms']==4000,item['id']
    assert item['duration_ms']==4000*len(item['steps']),item['id']
    assert all(item[k]==next(s for s in stories if s['id']==item['id'])[k]
               for k in ['nodes','links','steps','objective','scenario','tradeoff','topics']),item['id']
    with Image.open(root/item['gif']) as gif:
        assert gif.is_animated and gif.size==(1600,1000),item['id']
        assert gif.n_frames==item['encoded_frame_count'],item['id']
        duration=0
        for index in range(gif.n_frames):
            gif.seek(index)
            gif.load()
            assert gif.size==(1600,1000),item['id']
            frame_ms=gif.info.get('duration',0)
            assert frame_ms>0,item['id']
            # Encoding may merge identical motionless frames, never adjacent stages.
            assert duration//4000==(duration+frame_ms-1)//4000,(item['id'],duration,frame_ms)
            duration+=frame_ms
        assert duration==item['duration_ms'],(item['id'],duration)
        assert gif.info.get('loop')==0,item['id']
    with Image.open(root/item['static']) as still:
        still.load()
        assert still.size==(1600,1016*len(item['steps'])),item['id']
for path in list((root/'animations').glob('*.md'))+list((root/'curriculum').rglob('*.md'))+list((root/'practice').glob('*.md')):
    text=path.read_text(encoding='utf-8')
    for block in re.findall(r'<details\b[^>]*>.*?</details>',text,re.S):
        assert '.gif)' not in block,f'Animation hidden behind a toggle: {path}'
print(f'PASS: all {len(entries)} GIFs loop forever at exactly 4000 ms per stage; every frame decoded, stills checked, embeds visible by default.')
