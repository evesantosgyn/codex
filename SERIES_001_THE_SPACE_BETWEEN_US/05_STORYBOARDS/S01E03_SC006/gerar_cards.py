import json, os, hashlib, jsonschema
ROOT='/home/user/codex'; SER=ROOT+'/SERIES_001_THE_SPACE_BETWEEN_US'
OUT=SER+'/05_STORYBOARDS/S01E03_SC006/shots'; os.makedirs(OUT,exist_ok=True)
schema=json.load(open(ROOT+'/templates/shot-card.schema.json'))
IMG='06_GENERATED_ASSETS/IMAGES/'
KF=lambda n: IMG+f'TSBU_S01E03_SC006_SH{n:02d}_KF_V01.png'
def h(f):
    q=SER+'/'+f
    return hashlib.sha256(open(q,'rb').read()).hexdigest() if os.path.exists(q) else None
CREF=['02_CHARACTERS/CLAIRE_BENNETT/claire-bennett_identity-pack.webp',IMG+'S01E03_LOOK_CLAIRE_V01.png']
OREF=['02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png',IMG+'S01E03_LOOK_OLIVIA_V01.png']
LOC=['03_LOCATIONS/FABRICA_RESTAURACAO/fabrica_ref-escritorio-capataz.png',IMG+'S01E03_SC003_KF-OFFICE-WS_V02.png',IMG+'S01E03_PROP_PRANCHA-OBJETOS_V01.png']
CC='Claire L7: dark-brown hair with curtain bangs (never copper), brown eyes, dark-red silk blouse, NO coat (on the chair), watch LEFT wrist, ONE dark-red pendant, NO rings'
OC='Olivia L1: messy dark-blond bun, green-hazel eyes, olive shirt, no watch, ONE beauty mark below lower lip on her left side, camera tattoo inner LEFT forearm, no hard hat'
AX='Axis: Claire LEFT of the light table (back to the glass partition), Olivia RIGHT; Claire looks right; Olivia looks down at the table/laptop'
ROOM="Evening in the foreman's office after six: the sconce is OFF; the only real light is the glowing light table from below, its white filtered through orange negative bases so both faces share the same amber; beyond the glass partition the empty factory hall is dark blue with one work light on the floor."
TEARS='Tears: Claire level 2 (one tear, hidden) only in SH24; Olivia level 1 (eyes full, no tear falls).'
CL=lambda e:{'character_id':'CHR-CLAIRE','look_id':'L7','expression_ids':e}
OL=lambda e:{'character_id':'CHR-OLIVIA','look_id':'L1','expression_ids':e}
def card(n,dur,kf,framing,camera,lens,action,emotion,gaze,intent,prompt,chars,dialogue=None,sfx='',forbid=None,tears=0,reaction=None,last=None,cont=None):
    ids=[c['character_id'] for c in chars]
    refs=(CREF if 'CHR-CLAIRE' in ids else [])+(OREF if 'CHR-OLIVIA' in ids else [])
    c=[AX]+([CC] if 'CHR-CLAIRE' in ids else [])+([OC] if 'CHR-OLIVIA' in ids else [])+(cont or [])
    first=kf if isinstance(kf,str) else KF(kf)
    return {'shot_id':f'S01E03_SC006_SH{n:02d}','scene_id':'S01E03_SC006','revision':'V01','status':'approved',
     'owner':{'creative':'Evelin','technical':'Pedro'},
     'approval':{'creative':{'by':'Evelin','date':'2026-11-27','decision':'N49'},'technical':{'by':None,'date':None}},
     'direction':{'intent':intent,'action':action,'dialogue':dialogue or [],'emotion':emotion,'tears_level':tears,'gaze':gaze,'camera':camera,'framing':framing,'lens_reference':lens,'duration_s':dur,'reaction_of':reaction,'continuity':c,
       'sound':{'dialogue':'; '.join(f"{d['character']}: {d['line']}" for d in (dialogue or [])) or 'none','ambience':'Office at night; the empty hall muffled beyond the glass; the light-table hum','sfx':sfx,'music':''},
       'neutral_prompt':prompt+' '+ROOM+' '+TEARS,'forbidden':(forbid or [])+['the sconce lit','any text on screens except the approved photo'],'characters':chars},
     'assets':{'first_frame':first,'last_frame':last,'character_refs':refs,'voice_refs':(['06_GENERATED_ASSETS/VOICES/claire_bennett_voice-ref_v02.wav'] if dialogue and dialogue[0]['character']=='CLAIRE' else []),'location_refs':LOC,'asset_hashes':{}},
     'execution':{k:None for k in ['engine','checkpoint','precision','workflow_id','prompt','seed','fps','resolution','duration','take_id']},
     'post':{'restoration':None,'color_transform':None,'audio_stems':[],'edit_in':None,'edit_out':None},
     'audit':{k:None for k in ['license_id','gpu','runtime','cost','output_hash','qc_status','approval_date']}}
D=lambda who,line,dl,p:[{'character':who,'line':line,'delivery':dl,'pause_before_s':p,'on_screen':True}]
S=[
card(1,4,1,'From the dark empty hall through the glass partition','static','24mm','The office glows only with the light table; both bent over it','Quiet intimacy after hours','—','Everyone has gone; Claire stayed','Static wide from the dark blue factory hall, one work light on the floor; through the black-framed glass, the small office lit only by a glowing light table, two women bent over it.',[CL(['EXP-C-02']),OL(['EXP-O-03'])],sfx='Distant city; the hall echo'),
card(2,2,2,'Insert of the coat on the chair','static','50mm',"Claire's charcoal coat hangs on the chair; she hasn't put it on",'—','—','She chose to stay','Static insert in near darkness: a long charcoal wool coat hanging on the back of a chair, amber light grazing it.',[],sfx='—'),
card(3,2,3,"Olivia's hands",'static','50mm','She closes a sleeve and files it in the metal box','—','—','The work is ending','Static insert: hands (camera tattoo on inner left forearm, no watch) sliding a translucent negative sleeve into a worn metal box with luggage stickers.',[OL([])],sfx='Paper sleeve; the box'),
card(4,2.5,4,'Olivia close, three-quarter, amber from below','light handheld','85mm','Giving Claire a way out, gently','Tender','At Claire','She offers the exit','Subtle handheld close-up of Olivia lit from below in amber, the sconce dark behind her; tender, careful.',[OL(['EXP-O-14'])],dialogue=D('OLIVIA',"It's after six.",'gentle, giving her the way out; render in a 5-6 s clip',1.0)),
card(5,2.5,5,'Claire at table height on the loupe','static','50mm',"Doesn't look up",'Dry, defended','Down into the loupe','She stays without admitting it','Static at table height: Claire bent over the loupe, lit from below, dark blue glass behind her; she does not look up.',[CL(['EXP-C-07'])],dialogue=D('CLAIRE','I know what time it is.','dry, low, without looking up',1.5)),
card(6,2,4,'= SH04','light handheld','85mm','Olivia looks at her; Claire does not look up','A quiet ache','At Claire','She sees that Claire stayed','Subtle handheld close-up: Olivia looks at Claire one second too long, saying nothing.',[OL(['EXP-O-05'])]),
card(7,2,7,'From above, the box · hand','static','100mm macro','One sleeve left; her hand stops on it','—','—','She knows what is in it','Static top-down insert: the open metal box with a single sleeve left; Olivia\'s hand stops on it and stays.',[OL([])],sfx='Silence; the hum'),
card(8,2,4,'= SH04','light handheld','85mm','The beat before she takes it','Held breath','Down at the box','Deciding to show it','Subtle handheld close-up: Olivia, a held breath, eyes down at the box; she decides.',[OL(['EXP-O-23'])]),
card(9,2,IMG+'S01E03_SC003_KF-INS-SLEEVE_V02.png','From above, hands','static','50mm','She lays the strip on the glass','—','—','The last strip','Static insert: hands laying a 120 color negative strip on the glowing glass.',[OL([])],sfx='Paper on glass'),
card(10,2,5,'= SH05','static','50mm','Claire bends to the loupe','Focused','Into the loupe','She looks','Static at table height: Claire bends to the loupe.',[CL(['EXP-C-02'])],sfx='The loupe on glass'),
card(11,4,11,'Through the loupe','static','macro','In negative: a bed, a window, a sleeping face, long hair, no bangs','—','—','The photograph of her','Static: a circle of inverted color negative through a loupe on a glowing light table — a woman asleep in morning light, long hair, no bangs; the rest blurred.',[],sfx='Only the hum'),
card(12,4,5,'= SH05','static','50mm','Claire stays bent over the glass for a long time','Hit; still','Into the loupe','She recognizes herself','Static at table height: Claire stays bent over the loupe, completely still, for a long time.',[CL(['EXP-C-23'])]),
card(13,3,13,'Hands at the scanner','static','50mm','Unasked, Olivia feeds the strip into the scanner','—','—','She shows it whole','Static insert: Olivia\'s hands feeding a negative strip into a small film scanner by a laptop, at night.',[OL([])],sfx='Scanner click and motor'),
card(14,4,14,'Laptop insert','static','50mm','Positive on screen: Claire asleep at 28','—','—','Seven years ago','Static insert: a laptop on the dark table, the screen showing the approved photograph of a young woman asleep, soft morning light, unguarded.',[],sfx='The scanner stops; silence'),
card(15,3,15,'Two-shot at table height','static','35mm',"Claire straightens slowly; doesn't look at Olivia",'Hurt held; Olivia watching the photo','Claire down; Olivia at the screen','The question is coming','Static two-shot at table height: both faces in the same amber from the light table, not looking at each other, the laptop glowing between them.',[CL(['EXP-C-24']),OL(['EXP-O-49'])]),
card(16,3,16,'Claire close, three-quarter','static','85mm',"Low, without looking at Olivia",'Hurt behind control','Down','She names the morning','Static close-up of Claire in amber, eyes down, voice low and level.',[CL(['EXP-C-24'])],dialogue=D('CLAIRE','You took this the morning you left.','low, level, not looking at Olivia; about two words per second',2.0)),
card(17,3.5,4,'Olivia close, looking at the screen','light handheld','85mm','A long beat, then the truth','Eyes full','At the photograph','She does not deny it','Subtle handheld close-up: Olivia looks at the photograph, eyes filling; after a long beat, the truth.',[OL(['EXP-O-29'])],dialogue=D('OLIVIA','Yes.','after a long beat, quiet, eyes on the photo; render in a 5-6 s clip',2.5),reaction='R1: SH16 frame without dialogue under "Yes." — Claire listens without looking'),
card(18,3,16,'= SH16','static','85mm','Her voice drops','Level 1, voice lower','Down','The wound in one sentence','Static close-up: Claire, voice lower, eyes glistening.',[CL(['EXP-C-25'])],dialogue=D('CLAIRE','You could have woken me.','lower, the voice almost catching',2.0),tears=1),
card(19,3,15,'= SH15','static','35mm','A long silence; the table hums','Both holding it','Apart','The silence answers','Static two-shot at table height: neither moves; three seconds of silence.',[CL(['EXP-C-25']),OL(['EXP-O-49'])],sfx='Only the hum',tears=1),
card(20,2.5,4,'= SH17','light handheld','85mm','Looking at the photograph, not at Claire','Confession starting','At the photograph','The truth she never said','Subtle handheld close-up: Olivia looks at the photograph and begins.',[OL(['EXP-O-49'])],dialogue=D('OLIVIA',"If I'd woken you...",'slow, to the photograph',2.0),tears=1),
card(21,2,21,'Extreme close-up of her mouth','static','100mm macro','The breath','—','—','The breath before it','Static extreme close-up: Olivia\'s lips and chin in amber, the single beauty mark, a held breath.',[OL(['EXP-O-23'])],sfx='Her breath'),
card(22,2.5,4,'= SH17','light handheld','85mm','—','Confession','At the photograph','The love that never ended','Subtle handheld close-up: Olivia finishes, almost to herself.',[OL(['EXP-O-27'])],dialogue=D('OLIVIA',"...I wouldn't have gone.",'almost to herself, eyes full, no tear',0.5),tears=1),
card(23,2.5,23,'Claire close','static','85mm','She closes her eyes','Fighting it','Eyes closed','It lands','Static close-up: Claire closes her eyes; the face perfectly still.',[CL(['EXP-C-25'])],sfx='Music enters in the pause (one low sustained note)',tears=1,reaction='R2: under "...I wouldn\'t have gone."'),
card(24,5,24,'Claire close, profile against the dark glass','static','85mm','Opens wet eyes; one tear escapes; she turns her face to the dark glass (her reflection in it) and wipes it with the back of her hand','Level 2, hidden','To the dark glass','She refuses to break in front of her','Static close-up: Claire opens wet eyes, one tear escapes; she turns her face toward the dark glass partition, her reflection faint in it, and wipes the tear with the back of her left hand (watch on the wrist).',[CL(['EXP-C-26'])],sfx='Sleeve fabric',tears=2,forbid=['more than one tear','sobbing']),
card(25,3,25,'Olivia close','light handheld','85mm',"She sees it; she doesn't move toward her",'Eyes full, still','At Claire','She lets Claire have it','Subtle handheld close-up: Olivia looks at Claire, eyes full, and does not move.',[OL(['EXP-O-13'])],tears=1,forbid=['moving toward Claire']),
card(26,4,25,'= SH25','light handheld','85mm','Almost no voice','Vulnerable','At Claire','Seven years in one sentence','Subtle handheld close-up: Olivia, almost no voice, eyes full, no tear.',[OL(['EXP-O-39'])],dialogue=D('OLIVIA',"I've looked at it every year since.",'almost no voice; slow; music ducks out under the line',2.5),tears=1),
card(27,2,27,"Claire's hand on the glowing glass",'static','100mm macro','A slow breath; her hand reaches for the strip to put it away','—','—','She tries to end it','Static insert: Claire\'s left hand (white-dial watch, dark-red silk cuff, no rings) moves toward the negative strip on the glowing glass.',[CL([])],sfx='A slow breath'),
card(28,3,28,'The hands from above on the glowing glass','slow push-in (approved exception)','100mm macro',"Olivia's hand covers Claire's, flat on the glass. One second. Two",'—','—','The first deliberate touch','Slow push-in, top-down: Olivia\'s hand (no watch) rests flat on top of Claire\'s hand (watch on the left wrist, no rings) on the glowing light table. Nothing else moves.',[CL(['EXP-C-21']),OL(['EXP-O-18'])],sfx='Music returns, very low'),
card(29,3,29,'Claire close','static','85mm',"She doesn't pull away; eyes on their hands",'Still, not responding','Down at the hands','She lets it be','Static close-up: Claire, eyes lowered to their hands, breath stopped; she neither pulls away nor responds.',[CL(['EXP-C-21'])],forbid=['pulling away','responding to the touch']),
card(30,2,30,'Olivia close','light handheld','85mm','Looking at their hands','Eyes full','At the hands','She knows it can only last a second','Subtle handheld close-up: Olivia looks down at their hands, eyes full.',[OL(['EXP-O-18'])],tears=1),
card(31,2,28,'= SH28','static','100mm macro','Olivia lifts her hand first','—','—','She is the one who lets go','Static top-down: Olivia\'s hand lifts away; Claire\'s hand stays flat on the glowing glass.',[CL([]),OL([])],last=KF(31)),
card(32,2.5,32,'Olivia close','light handheld','85mm','The loss already in her face','Loss','Down','She let go','Subtle handheld close-up: Olivia, eyes lowered, the loss already on her face.',[OL(['EXP-O-19'])],tears=1),
card(33,4,15,'= SH15','static','35mm','Neither speaks','Still','Apart','Nothing more can be said tonight','Static two-shot at table height: both in the same amber, silent; then cut.',[CL(['EXP-C-21']),OL(['EXP-O-19'])],sfx='Music out on the cut'),
]
for c in S:
    a=c['assets']; fs=a['character_refs']+a['voice_refs']+a['location_refs']
    a['asset_hashes']={f:h(f) for f in fs if h(f)}
    assert all(h(f) for f in fs), [f for f in fs if not h(f)]
    jsonschema.validate(c,schema)
    json.dump(c,open(f"{OUT}/TSBU_S01E03_SC006_SH{c['shot_id'][-2:]}_CARD_V01.json",'w'),indent=2,ensure_ascii=False)
print(len(S),'cards valid; total',sum(c['direction']['duration_s'] for c in S),'s')
