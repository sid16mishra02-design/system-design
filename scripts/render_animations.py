"""Render authored architecture walkthroughs: exactly one second per stage, infinite loop.

Explanatory storyboards, not measurements or protocol simulators.
Definitions: metadata/animation-stories.json. Dependency: Pillow.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache
import argparse, hashlib, json, math, re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'assets/animations'
W, H = 1600, 1000
FRAMES_PER_STEP, FRAME_MS = 20, 50
STEP_MS = FRAMES_PER_STEP * FRAME_MS
INK, MUTED, BLUE, TEAL, RED, AMBER, BG = '#172D49', '#536782', '#2467E8', '#07866F', '#C44251', '#B26A0C', '#EDF3FC'
FONT = next((p for p in ['C:/Windows/Fonts/segoeui.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'] if Path(p).exists()), 'DejaVuSans.ttf')
BOLD = next((p for p in ['C:/Windows/Fonts/seguisb.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'] if Path(p).exists()), FONT)

@lru_cache(maxsize=48)
def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)

def lines(draw, text, size, width, bold=False):
    result, current = [], ''
    for word in text.split():
        trial = (current + ' ' + word).strip()
        if draw.textlength(trial, font=font(size, bold)) > width and current:
            result.append(current)
            current = word
        else:
            current = trial
    if current: result.append(current)
    return result

def write(draw, xy, text, size, width, color=INK, bold=False, maxlines=3, leading=None):
    rows = lines(draw, text, size, width, bold)
    assert len(rows) <= maxlines, (text, rows, width)
    leading = leading or size + 5
    for i, row in enumerate(rows):
        draw.text((xy[0], xy[1] + i * leading), row, font=font(size, bold), fill=color)
    return len(rows) * leading

def card(draw, box, fill='white', outline=None, radius=18, shadow=True, width=1):
    x1, y1, x2, y2 = box
    if shadow:
        draw.rounded_rectangle((x1+1, y1+5, x2+1, y2+5), radius=radius, fill='#DEE7F4')
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def arrow(draw, points, color, width=3):
    draw.line(points, fill=color, width=width, joint='curve')
    a, b = points[-2:]
    angle = math.atan2(b[1]-a[1], b[0]-a[0])
    length = 11
    draw.polygon([b, (b[0]-length*math.cos(angle-.5), b[1]-length*math.sin(angle-.5)),
                  (b[0]-length*math.cos(angle+.5), b[1]-length*math.sin(angle+.5))], fill=color)

def path_at(points, fraction):
    distances = [math.dist(a,b) for a,b in zip(points,points[1:])]
    left = sum(distances)*max(0,min(1,fraction))
    for a,b,length in zip(points,points[1:],distances):
        if left<=length and length:
            return (a[0]+(b[0]-a[0])*left/length, a[1]+(b[1]-a[1])*left/length)
        left-=length
    return points[-1]

def node_box(node):
    x,y = 58+278*node['col'], 277+252*node['row']
    return x,y,x+234,y+132

def route(link,nodes,index):
    a,b = nodes[link['from']],nodes[link['to']]
    ax1,ay1,ax2,ay2=node_box(a); bx1,by1,bx2,by2=node_box(b)
    ax,ay,bx,by=(ax1+ax2)/2,(ay1+ay2)/2,(bx1+bx2)/2,(by1+by2)/2
    if a['row']==b['row']:
        if abs(a['col']-b['col'])==1:
            off=-18 if b['col']>a['col'] else 18
            return [(ax2 if bx>ax else ax1,ay+off),(bx1 if bx>ax else bx2,by+off)]
        lane=ay1-18-10*(index%3) if a['row']==0 else ay2+24+10*(index%3)
        return [(ax,ay1 if a['row']==0 else ay2),(ax,lane),(bx,lane),(bx,by1 if a['row']==0 else by2)]
    if a['col']==b['col']:
        off=-20 if by>ay else 20
        return [(ax+off,ay2 if by>ay else ay1),(bx+off,by1 if by>ay else by2)]
    lane=440+11*(index%5)
    return [(ax,ay2 if by>ay else ay1),(ax,lane),(bx,lane),(bx,by1 if by>ay else by2)]

def icon(draw,x,y,label,color):
    name=label.lower()
    if any(t in name for t in ['database','store','history','record','log','replica','shard','index']):
        draw.rectangle((x,y+5,x+25,y+23),fill='white',outline=color,width=2)
        draw.ellipse((x,y,x+25,y+10),fill='white',outline=color,width=2)
        draw.arc((x,y+17,x+25,y+27),0,180,fill=color,width=2)
    elif any(t in name for t in ['queue','topic','stream','cache','bucket']):
        for k in range(3):
            draw.rounded_rectangle((x,y+9*k,x+27,y+7+9*k),radius=2,outline=color,width=2)
            draw.ellipse((x+4,y+2+9*k,x+6,y+4+9*k),fill=color)
    elif any(t in name for t in ['client','browser','user','buyer','rider','player','viewer']):
        draw.rounded_rectangle((x,y,x+27,y+20),radius=3,outline=color,width=2)
        draw.line((x+14,y+21,x+14,y+26),fill=color,width=2)
        draw.line((x+5,y+27,x+23,y+27),fill=color,width=2)
    else:
        draw.rounded_rectangle((x,y,x+27,y+27),radius=6,outline=color,width=2)
        for ox,oy in [(6,6),(17,6),(6,17),(17,17)]:
            draw.rectangle((x+ox,y+oy,x+ox+4,y+oy+4),fill=color)

def mechanism(draw,step):
    card(draw,(30,736,1178,884),shadow=False,fill='#E2ECFA')
    draw.text((52,749),'INSIDE THE MECHANISM',font=font(15,True),fill=MUTED)
    visual=step.get('visual',{});kind=visual.get('kind')
    detail_x,detail_w=52,1090
    if kind=='bits':
        for i,bit in enumerate(visual['bits']):
            x,y=54+i*46,791
            draw.rounded_rectangle((x,y,x+37,y+38),radius=6,fill=BLUE if bit else 'white',
                outline=AMBER if i in visual.get('probe',[]) else '#B5C8E3',width=3)
            draw.text((x+12,y+3),str(bit),font=font(21,True),fill='white' if bit else INK)
            draw.text((x+13,y+42),str(i),font=font(12),fill=MUTED)
        write(draw,(623,778),visual.get('result',''),20,505,BLUE,True,2)
        write(draw,(623,838),step['detail'][0],17,505,maxlines=2)
        return
    if kind=='ring':
        cx,cy,r=160,817,48
        draw.ellipse((cx-r,cy-r,cx+r,cy+r),outline='#9AB3D8',width=3)
        if visual.get('highlight'):
            start,end=visual['highlight']
            draw.arc((cx-r,cy-r,cx+r,cy+r),start-90,end-90,fill=TEAL,width=7)
        for member in visual.get('members',[]):
            angle=math.radians(member['angle']);x,y=cx+r*math.sin(angle),cy-r*math.cos(angle)
            draw.ellipse((x-7,y-7,x+7,y+7),fill=BLUE)
            tx,ty=cx+(r+24)*math.sin(angle),cy-(r+16)*math.cos(angle)
            draw.text((tx-8,ty-9),member['label'],font=font(15,True),fill=INK)
        for key in visual.get('keys',[]):
            angle=math.radians(key['angle']);x,y=cx+(r-10)*math.sin(angle),cy-(r-10)*math.cos(angle)
            draw.ellipse((x-4,y-4,x+4,y+4),fill=AMBER)
        detail_x,detail_w=300,840
    elif kind=='grid':
        x0,y0,cw,ch=58,782,43,26
        for col in range(5):
            for row in range(3):
                selected=[col,row] in visual.get('cells',[])
                draw.rectangle((x0+col*cw,y0+row*ch,x0+(col+1)*cw,y0+(row+1)*ch),
                    fill='#BFD8FC' if selected else 'white',outline='#A3BADA')
        for x,color in [(x0+3*cw-8,BLUE),(x0+3*cw+8,TEAL)]:
            draw.ellipse((x-4,y0+ch+8,x+4,y0+ch+16),fill=color)
        draw.text((296,785),'Rider | nearby driver',font=font(17,True),fill=INK)
        draw.text((296,815),'Cell boundary ≠ distance',font=font(16),fill=MUTED)
        detail_x,detail_w=605,530
    elif kind=='lanes':
        for j,lane in enumerate(visual.get('lanes',[])[:3]):
            y=780+j*30
            draw.text((54,y),lane['label'],font=font(15,True),fill=INK)
            for i,value in enumerate(lane['cells'][:4]):
                x=165+i*61
                color=BLUE if value=='A' else TEAL if value=='B' else '#C9D7EC'
                draw.rounded_rectangle((x,y,x+54,y+24),radius=4,fill=color)
                draw.text((x+21,y+1),value,font=font(15,True),fill='white')
        detail_x,detail_w=475,660
    if kind:
        for i,fact in enumerate(step['detail'][:3]):
            write(draw,(detail_x,778+i*30),fact,18,detail_w,maxlines=1)
    else:
        for i,fact in enumerate(step['detail'][:3]):
            x=52+i*372
            draw.rounded_rectangle((x,782,x+349,866),radius=10,fill='white')
            draw.text((x+12,791),f'{i+1:02}',font=font(16,True),fill=TEAL)
            write(draw,(x+45,791),fact,19,289,maxlines=3,leading=23)

def scene(story,index,state):
    step=story['steps'][index];warning=step.get('warning',False)
    color=RED if warning else BLUE
    image=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(image)
    for y in range(126):
        t=y/125
        d.line((0,y,W,y),fill=(int(19+10*t),int(39+15*t),int(67+21*t)))
    d.text((32,13),'SYSTEM DESIGN  /  CONCEPT IN MOTION',font=font(14,True),fill='#9ABDED')
    title_size=34 if len(story['title'])<65 else 29
    write(d,(30,34),story['title'],title_size,1500,'white',True,1)
    write(d,(32,84),story['objective'],21,1500,'#CBDAED',maxlines=1)
    card(d,(30,145,1178,213),radius=14,shadow=False)
    d.rounded_rectangle((42,157,131,201),radius=11,fill=color)
    d.text((59,163),f'{index+1:02} / {len(story["steps"]):02}',font=font(19,True),fill='white')
    write(d,(149,153),step['title'],22,992,INK,True,1)
    write(d,(149,182),step['caption'],17,995,MUTED,maxlines=1)
    card(d,(1198,145,1570,213),radius=14,shadow=False,fill='#DCE9FC')
    d.text((1219,155),'1 SECOND / STEP',font=font(18,True),fill=BLUE)
    d.text((1219,183),'Automatic playback · repeats',font=font(17),fill=MUTED)
    card(d,(30,230,1178,718))
    for x in range(48,1170,20):
        for y in range(244,710,20):d.ellipse((x,y,x+1,y+1),fill='#DCE5F2')
    nodes={n['id']:n for n in story['nodes']}
    routes=[route(link,nodes,i) for i,link in enumerate(story['links'])]
    active=set(step['active'])
    for points in routes:arrow(d,points,'#CBD7E8',2)
    for i in active:arrow(d,routes[i],color,4)
    focused={key for i in active for key in [story['links'][i]['from'],story['links'][i]['to']]}
    for node in story['nodes']:
        x1,y1,x2,y2=node_box(node);changed=node['id'] in step['updates'];selected=node['id'] in focused or changed
        outline=color if selected else '#B9CAE1'
        card(d,(x1,y1,x2,y2),outline=outline,radius=15,width=3 if selected else 1)
        d.rounded_rectangle((x1+11,y1+10,x1+50,y1+49),radius=9,fill='#EEF4FD')
        icon(d,x1+17,y1+16,node['label'],color if selected else MUTED)
        write(d,(x1+60,y1+11),node['label'],20,166,INK,True,2,23)
        write(d,(x1+14,y1+58),node['role'],15,207,MUTED,maxlines=1)
        d.rounded_rectangle((x1+9,y1+82,x2-9,y2-8),radius=7,
            fill='#FDE9EC' if warning and changed else '#E4F4EE' if changed else '#F0F4FA')
        write(d,(x1+16,y1+85),state[node['id']],17,198,
            RED if warning and changed else TEAL if changed else INK,True,2,19)
    label_boxes=[]
    for i in active:
        x,y=path_at(routes[i],.5);label=story['links'][i]['label'];tw=d.textlength(label,font=font(15,True))
        source=nodes[story['links'][i]['from']];target=nodes[story['links'][i]['to']]
        if source['row']==target['row']:
            y=274 if source['row']==0 else 525
        x=max(42+tw/2,min(1166-tw/2,x))
        box=(x-tw/2-7,y-29,x+tw/2+7,y-5)
        if any(box[0]<b[2] and box[2]>b[0] and box[1]<b[3] and box[3]>b[1] for b in label_boxes):
            x=max(42+tw/2,min(1166-tw/2,x+tw+18));box=(x-tw/2-7,y-29,x+tw/2+7,y-5)
        label_boxes.append(box)
        d.rounded_rectangle(box,radius=6,fill='white',outline='#D4E0F0')
        d.text((x-tw/2,y-27),label,font=font(15,True),fill=color)
    card(d,(1198,230,1570,884))
    d.text((1220,253),'WHERE IT FITS',font=font(15,True),fill=BLUE)
    write(d,(1220,281),story['scenario'],22,326,INK,True,4)
    d.line((1220,406,1548,406),fill='#DCE5F2',width=2)
    d.text((1220,427),'WHAT CHANGES NOW',font=font(15,True),fill=color)
    write(d,(1220,456),step['insight'],22,326,INK,True,5)
    d.line((1220,616,1548,616),fill='#DCE5F2',width=2)
    d.text((1220,639),'DESIGN TRADEOFF',font=font(15,True),fill=AMBER)
    write(d,(1220,669),story['tradeoff'],21,326,MUTED,maxlines=6)
    d.text((1220,846),'Blue: active   Red: risk / failure',font=font(15),fill=MUTED)
    mechanism(d,step)
    count=len(story['steps']);gap=7;width=(1540-gap*(count-1))/count
    for j,s in enumerate(story['steps']):
        x=30+j*(width+gap)
        fill=color if j==index else '#BED2ED' if j<index else '#DBE5F3'
        d.rounded_rectangle((x,908,x+width,916),radius=4,fill=fill)
        write(d,(x,923),f'{j+1:02}  {s["title"]}',14,width-5,INK if j==index else MUTED,j==index,2,18)
    d.text((30,976),'Illustrative architecture · Timing shows the teaching sequence, not system performance · Text and stills below',font=font(14),fill=MUTED)
    return image,routes

def animate(base,routes,step,phase):
    image=base.copy().convert('RGBA');layer=Image.new('RGBA',image.size);d=ImageDraw.Draw(layer)
    color=(196,66,81) if step.get('warning') else (36,103,232)
    for i in step['active']:
        for lag,radius,alpha in [(.12,5,65),(.06,6,130),(0,7,255)]:
            x,y=path_at(routes[i],max(0,phase-lag))
            if lag==0:
                d.ellipse((x-15,y-15,x+15,y+15),fill=(*color,28))
                d.ellipse((x-11,y-11,x+11,y+11),fill=(*color,55))
            d.ellipse((x-radius,y-radius,x+radius,y+radius),fill=(*color,alpha))
        d.ellipse((x-2,y-2,x+2,y+2),fill='white')
    return Image.alpha_composite(image,layer).convert('RGB')

def render(story):
    state={n['id']:n['initial'] for n in story['nodes']};frames=[];stills=[]
    for i,step in enumerate(story['steps']):
        state.update(step['updates']);base,routes=scene(story,i,state);stills.append(base)
        for j in range(FRAMES_PER_STEP):
            im=animate(base,routes,step,(j+.5)/FRAMES_PER_STEP)
            frames.append(im.quantize(colors=128,method=Image.Quantize.FASTOCTREE))
    path=DEST/(story['id']+'.gif')
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=FRAME_MS,loop=0,optimize=True,disposal=1)
    # Full-resolution states in one column preserve small diagram labels.
    board=Image.new('RGB',(W,(H+16)*len(stills)),BG)
    for i,im in enumerate(stills):board.paste(im,(0,i*(H+16)))
    static=DEST/(story['id']+'-steps.png');board.save(static,optimize=True)
    with Image.open(path) as encoded:encoded_count=encoded.n_frames
    word_count=lambda text:len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b",text))
    return {**story,'gif':f'assets/animations/{story["id"]}.gif','static':f'assets/animations/{story["id"]}-steps.png',
        'width':W,'height':H,'step_duration_ms':STEP_MS,'duration_ms':STEP_MS*len(story['steps']),
        'frame_count':len(frames),'encoded_frame_count':encoded_count,
        'gif_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'static_sha256':hashlib.sha256(static.read_bytes()).hexdigest(),
        'caption_words':sum(word_count(s['caption']) for s in story['steps'])}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only',help='Render one storyboard ID')
    parser.add_argument('--missing',action='store_true',help='Render IDs absent from the output manifest')
    args=parser.parse_args()
    stories=json.loads((ROOT/'metadata/animation-stories.json').read_text(encoding='utf-8'))
    manifest_path=ROOT/'metadata/animations.json'
    old={s['id']:s for s in json.loads(manifest_path.read_text(encoding='utf-8'))} if manifest_path.exists() else {}
    manifest=[];DEST.mkdir(exist_ok=True,parents=True)
    for story in stories:
        if (args.only and story['id']!=args.only) or (args.missing and story['id'] in old):
            if story['id'] in old:manifest.append(old[story['id']])
            continue
        manifest.append(render(story));print('Rendered',story['id'],flush=True)
        partial={**old,**{s['id']:s for s in manifest}}
        manifest_path.write_text(json.dumps([partial[s['id']] for s in stories if s['id'] in partial],indent=2)+'\n',encoding='utf-8')
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Rendered {len(manifest)} walkthroughs, {STEP_MS} ms per step, infinite loop.')

if __name__=='__main__': main()
