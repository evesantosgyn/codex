import json, os, sys, jsonschema, hashlib
def h(f):
    q=SER+'/'+f
    return hashlib.sha256(open(q,'rb').read()).hexdigest() if os.path.exists(q) else None
ROOT='/home/user/codex'; SER=ROOT+'/SERIES_001_THE_SPACE_BETWEEN_US'
OUT=SER+'/05_STORYBOARDS/S01E03_SC005/shots'; os.makedirs(OUT,exist_ok=True)
schema=json.load(open(ROOT+'/templates/shot-card.schema.json'))
IMG='06_GENERATED_ASSETS/IMAGES/'
KF=lambda n: IMG+f'TSBU_S01E03_SC005_SH{n:02d}_KF_V01.png'
MAYA=['02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg',IMG+'S01E03_LOOK_MAYA_V01.png']
JUNE=['02_CHARACTERS/JUNE_PARK/june_ref-SC005_KF-J1.png',IMG+'S01E03_LOOK_JUNE_V01.png']
CO=[IMG+'S01E03_LOOK_CLAIRE_V01.png',IMG+'S01E03_LOOK_OLIVIA_V01.png']
LOC=['03_LOCATIONS/FABRICA_RESTAURACAO/fabrica_ref-salao.png','03_LOCATIONS/FABRICA_RESTAURACAO/fabrica_ref-escritorio-capataz.png',IMG+'S01E03_SC001_KF-HALL-WS_V01.png',IMG+'S01E03_SC003_KF-OFFICE-WS_V02.png']
VM=['06_GENERATED_ASSETS/VOICES/maya_reed_voice-ref_v02.wav']
CONT_M='Maya: EP03 L1 brown tweed, black blouse, watch on LEFT wrist, hoops; white hard hat, no text; chin-length copper curls, green eyes'
CONT_J='June: EP03 L5 burgundy chunky sweater, black trousers, badge lanyard, dark-strap watch on LEFT wrist; white hard hat, no text; straight dark hair loose at collarbone; black cable'
CONT_G='Through the glass: Claire (dark-brown hair with curtain bangs, dark-red silk blouse, ONE dark-red pendant, watch LEFT wrist, NO rings) and Olivia (messy dark-blond bun, olive shirt, no watch), no hard hats, bent over the white light table'
AXIS='Axis: Maya LEFT, June RIGHT; between them Maya looks right, June looks left; the glass is in front of both'
NOSMILE='Maya smiling (not even in the eyes)'
HALL='Late afternoon in the main hall of the old brick factory: cool grey-blue daylight overall, with a few low golden sunbeams slanting through the high west windows and dust in the air; beyond the black-framed glass partition, the foreman\'s office with a white glowing light table and a warm sconce.'
SND_AMB='Empty factory hall: big echo, pigeons in the rafters, a distant hammer'
def card(n,dur,kf,framing,camera,lens,action,emotion,gaze,intent,prompt,dialogue=None,chars='M',cont=None,sfx='',forbid=None,tears=0,reaction=None,voice=False,last=None):
    refs=[]; c=[AXIS]
    if 'M' in chars: refs+=MAYA; c.append(CONT_M)
    if 'J' in chars: refs+=JUNE; c.append(CONT_J)
    if 'G' in chars: refs+=CO; c.append(CONT_G)
    if cont: c+=cont
    return {
     'shot_id':f'S01E03_SC005_SH{n:02d}','scene_id':'S01E03_SC005','revision':'V01','status':'approved',
     'owner':{'creative':'Evelin','technical':'Pedro'},
     'approval':{'creative':{'by':'Evelin','date':'2026-11-25','decision':'N48'},'technical':{'by':None,'date':None}},
     'direction':{'intent':intent,'action':action,'dialogue':dialogue or [],'emotion':emotion,'tears_level':tears,'gaze':gaze,
       'camera':camera,'framing':framing,'lens_reference':lens,'duration_s':dur,'reaction_of':reaction,'continuity':c,
       'sound':{'dialogue':'; '.join(f"{d['character']}: {d['line']}" for d in (dialogue or [])) or 'none','ambience':SND_AMB,'sfx':sfx,'music':'none'},
       'neutral_prompt':prompt+' '+HALL,'forbidden':(forbid or [])+['any text on hard hats','music']},
     'assets':{'first_frame':KF(kf),'last_frame':last,'character_refs':refs,'voice_refs':VM if voice else [],'location_refs':LOC,'asset_hashes':{}},
     'execution':{k:None for k in ['engine','checkpoint','precision','workflow_id','prompt','seed','fps','resolution','duration','take_id']},
     'post':{'restoration':None,'color_transform':None,'audio_stems':[],'edit_in':None,'edit_out':None},
     'audit':{k:None for k in ['license_id','gpu','runtime','cost','output_hash','qc_status','approval_date']}}
S=[
card(1,4,1,'Over Maya\'s shoulder (soft, foreground left) through the glass partition','static','35mm','Inside the office Claire and Olivia bend over the light table, not speaking, not looking at each other','Quiet tension seen from outside','Maya looks through the glass at Claire','The glass is the stage: the friends watch what they cannot hear',
 'Static shot over the soft-focus shoulder of a woman in a white hard hat and brown tweed (Maya, copper curls). Through a black-framed glass partition, two women bend over a glowing white light table without speaking. Nothing moves except dust in the light.',chars='MG',sfx='The light-table hum, muffled by the glass',forbid=['Claire or Olivia talking or touching','Maya in focus']),
card(2,3,2,'Maya, waist up, frontal, a little wider','static','50mm','Arms crossed, watching the office through the glass; not a muscle moves','Suspicion and worry held still; for once, no joke','Toward the glass, just off camera','The comic friend has stopped joking',
 'Static medium shot. Maya, arms crossed, white hard hat, brown tweed blazer, looks just off camera toward the glass partition. Serious, completely still, jaw set. No smile, not even in the eyes. Golden side light.',chars='M',sfx='Tweed rustle as she crosses her arms',forbid=[NOSMILE,'gesturing']),
card(3,2,3,'June on the right edge of frame, profile','light handheld','85mm','June arrives and stops beside Maya, coiling a black cable around her forearm','Calm, loyal, busy hands','Toward the glass','June arrives already knowing',
 'Subtle handheld, June framed at the right edge, in profile: white hard hat, burgundy chunky sweater, straight dark hair at the collarbone. She steps in and stops, coiling a black cable around her forearm, eyes on the glass.',chars='J',sfx='Footsteps stopping; the cable sliding over the sweater sleeve',forbid=['deadpan comedy','looking at camera']),
card(4,2,2,'= SH02','static','50mm','Without taking her eyes off the glass','Low, direct, protective','Toward the glass','Maya asks the question the audience already knows the answer to',
 'Static. Maya, arms crossed, eyes on the glass, asks low and direct: "What did she do?" She speaks slowly, without looking at June. No smile.',dialogue=[{'character':'MAYA','line':'What did she do?','delivery':'low, direct, not looking at June','pause_before_s':1.0,'on_screen':True}],chars='M',forbid=[NOSMILE],voice=True),
card(5,2,5,'June profile, closer','light handheld','85mm','Still coiling the cable','Honest; not hers to tell','Through the glass, at Olivia','June refuses without lying',
 'Subtle handheld profile close-up. June keeps coiling the cable and says simply, without looking away from the glass: "Not my story." Not defensive, not funny. Slow.',dialogue=[{'character':'JUNE','line':'Not my story.','delivery':'simple, honest, not defensive; render in a 5-6 s clip so it is not rushed','pause_before_s':1.0,'on_screen':True}],chars='J',sfx='Cable sliding',forbid=['deadpan comedy'],reaction='R1: SH02_KF without dialogue under this line — Maya does not look away'),
card(6,1.5,2,'= SH02','static','50mm','—','Pushing, quiet','Toward the glass','Maya pushes once',
 'Static. Maya, still watching the glass, quietly: "Then whose?" A short line, delivered without hurry. No smile.',dialogue=[{'character':'MAYA','line':'Then whose?','delivery':'quiet, pushing; render in a 5-6 s clip','pause_before_s':1.0,'on_screen':True}],chars='M',forbid=[NOSMILE],voice=True),
card(7,2,5,'= SH05','light handheld','85mm','June looks through the glass at Olivia; her hands slow on the cable','Tenderness for her friend','Through the glass, at Olivia','June looks at the person whose story it is',
 'Subtle handheld profile close-up. June looks through the glass at Olivia; her face softens with care. Her hands slow on the cable. Silence.',chars='J',sfx='Cable sliding, slower'),
card(8,4,5,'= SH05','light handheld','85mm','Low, with tenderness for her friend','A request, not an excuse','Through the glass, at Olivia','June asks Maya to wait',
 'Subtle handheld profile close-up. Low and warm, still looking at Olivia: "Hers. She\'s going to tell it." A held beat. "Give her time." It is a request, not an excuse.',dialogue=[{'character':'JUNE','line':"Hers. She's going to tell it. [pause] Give her time.",'delivery':'low, tender toward Olivia; a real beat before "Give her time."','pause_before_s':1.5,'on_screen':True}],chars='J',sfx='Cable sliding'),
card(9,2,9,'Maya close-up, turned to her right (toward June)','static','85mm','Maya turns her head to June and holds','The joke never comes; the hurt for Claire does','At June, frame right','The turn: Maya finally looks away from the glass',
 'Static close-up. Maya slowly turns her face to her right, toward June, and holds. Serious, still, eyes beginning to glisten. No smile. 1.5 to 2 seconds of silence.',chars='M',forbid=[NOSMILE],tears=1),
card(10,3,9,'= SH09','static','85mm','Low, no joke in it','Seven years of watching her friend carry it','At June','The line that names the cost',
 'Static close-up. Maya, facing June, low and firm, slower than usual, no joke in it: "She gave her seven years." Her eyes glisten slightly; no tear. She does not move.',dialogue=[{'character':'MAYA','line':'She gave her seven years.','delivery':'quiet, no joke in it; about two words per second','pause_before_s':2.0,'on_screen':True}],chars='M',forbid=[NOSMILE,'tears falling'],tears=1,voice=True),
card(11,2,11,'Insert: June\'s hands on the cable','static','100mm macro','Her hands stop coiling','The answer is the stop','—','June\'s answer is a gesture',
 'Static insert. June\'s hands, burgundy sleeves, dark-strap watch on her LEFT wrist, stop in the middle of coiling a black cable and stay still.',chars='J',sfx='The cable stops; then only the hall',forbid=['hands moving after they stop']),
card(12,3,12,'June close-up from the edge','light handheld','85mm','She has no answer and doesn\'t pretend to; her eyes lower','She knows Maya is right','Down','June has nothing to say',
 'Subtle handheld close-up from the edge of frame. June has no answer and does not pretend to have one. Her eyes lower; her mouth stays closed. Two seconds of only the hall.',chars='J',forbid=['speaking','smiling'],reaction='R2: this frame without dialogue under "She gave her seven years."'),
card(13,2,13,'From inside the office, through the glass: the two side by side','static','35mm','Both look in, silent; soft reflection of the light table on the glass','Two loyalties, side by side, both right','Toward camera (into the office)','The reverse: the friends seen as the couple would see them',
 'Static, from inside the office through the glass partition: Maya (left, tweed, hard hat) and June (right, burgundy, hard hat, cable) stand side by side in the golden hall, looking in, silent. Soft reflections of the light table and the warm sconce on the glass.',chars='MJ',sfx='The hall muffled by the glass; the light-table hum in the room',forbid=[NOSMILE,'reflections hiding the faces']),
card(14,1.5,2,'= SH02','static','50mm','Maya looks back at the glass','Resignation; she will wait, for Claire','Toward the glass','Back to watching',
 'Static. Maya turns back to the glass and keeps watching, arms crossed. No smile.',chars='M',forbid=[NOSMILE]),
card(15,3,15,'Through the glass, closer','static','35mm','Inside, Claire glances at the watch on her LEFT wrist; Olivia, bent over the light table, doesn\'t notice','Time is running out','Claire: down at her watch','Bridge to SC006: the hour is coming',
 'Static, from the hall through the black-framed glass, closer: inside, Claire glances at the watch on her LEFT wrist. Beside her, Olivia stays bent over the light table and does not notice. Then cut.',chars='G',sfx='The hall; the light-table hum muffled',forbid=['Claire or Olivia talking','Olivia looking up']),
]
for c in S:
    a=c['assets']; a['asset_hashes']={f:h(f) for f in a['character_refs']+a['voice_refs']+a['location_refs'] if h(f)}
    missing=[f for f in a['character_refs']+a['voice_refs']+a['location_refs'] if not h(f)]
    assert not missing, missing
    jsonschema.validate(c,schema)
    n=c['shot_id'][-2:]
    json.dump(c,open(f'{OUT}/TSBU_S01E03_SC005_SH{n}_CARD_V01.json','w'),indent=2,ensure_ascii=False)
print(len(S),'cards valid; total',sum(c['direction']['duration_s'] for c in S),'s')
