"""Decode every animation and still; validate frame count, duration, and bounds."""
from pathlib import Path
from PIL import Image
import json

root=Path(__file__).resolve().parents[1]
entries=json.loads((root/'metadata/animations.json').read_text(encoding='utf-8'))
for item in entries:
    with Image.open(root/item['gif']) as gif:
        assert gif.is_animated and gif.size==(960,600),item['id']
        assert gif.n_frames==item['encoded_frame_count'],item['id']
        duration=0
        for index in range(gif.n_frames):
            gif.seek(index)
            gif.load()
            assert gif.size==(960,600),item['id']
            duration+=gif.info.get('duration',0)
        assert duration==item['duration_ms'],(item['id'],duration)
        assert gif.info.get('loop')==0,item['id']
    with Image.open(root/item['static']) as still:
        still.load()
        assert still.width>0 and still.height>0,item['id']
print(f'PASS: decoded all frames of {len(entries)} GIFs, plus {len(entries)} still storyboards; durations and frame counts match.')
