# Pacote de geração no H3 — S01E01 · SC001 "Everything Under Control" (refação)

**Plataforma:** buzzy.now · **Modelo:** MiniMax-H3 · **Data:** 2026-11-12
**Base:** decupagem V03 (APROVADA) + 16 keyframes aprovados + método de fala A (P-13). Animatic: `07_EDITING/S01E01_SC001_animatic_V03.mp4`.

## Antes de cada geração (sempre)
1. **16:9.** Confira, porque o teste saiu em 21:9.
2. **480p** só para teste; o plano aprovado é gerado na maior resolução disponível.
3. Duração: o mínimo da plataforma (4–5 s), salvo indicação; o corte fino é feito na montagem.
4. Troque cada `@NOME` pela **etiqueta do arquivo**, no lugar exato do texto.
5. Salve como `S01E01_SC001_SH##_V##.mp4`.

## Arquivos (ter à mão)
| Etiqueta | Arquivo |
|---|---|
| `@ID_CLAIRE` | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` |
| `@VOZ_CLAIRE` | `06_GENERATED_ASSETS/VOICES/claire_bennett_voice-ref_v02.wav` |
| `@ID_MAYA` | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` |
| `@VOZ_MAYA` | `06_GENERATED_ASSETS/VOICES/maya_reed_voice-ref_v02.wav` |
| `@KF-…` | `06_GENERATED_ASSETS/IMAGES/S01E01_SC001_KF-…` (C1, C2, TELE e DEEP = **V02**; 2S = **V03**; FOLDER-TOP = **V02**; o resto = V01) |

## Modos
- **SF = Start & end frame:** planos sem fala; o keyframe vai como primeiro quadro.
- **OR = Omni Reference:** planos com fala; keyframe + identidade + voz de quem fala.

**Frase final de todo prompt (copiar no fim):** *Claire's hair stays dark chocolate brown, long and wavy with curtain bangs, wine-red lipstick. Maya's hair stays curly and chin-length. Golden-hour sunset light stays the same. Natural hands. No on-screen text except the studio logo. No music.*

**Bloco de fala** (planos OR): *Use @KF-… as the opening frame and composition. Keep the identities of @ID_CLAIRE / @ID_MAYA. Use @VOZ_CLAIRE / @VOZ_MAYA only as the reference for each woman's voice.*

---

## Planos

### SH01 · SF · início `KF-TOP` → fim `KF-2S` · 6 s
> High angle over the white architectural model. A woman's fingers place the smallest model tree near the entrance, then withdraw. The camera slowly rises and pulls back, revealing two women seated facing each other across the desk at golden hour, the sunset skyline behind them. Sound: quiet office ambience.
*Plano B: se a subida falhar, gerar só o KF-TOP estático (4 s) e cortar para o SH03.*

### SH02 · SF · `KF-INS-TREE` · 4 s
> Static macro. Her fingers make a minute adjustment to the tiny model tree, then hold still. Shallow depth of field, warm light. Sound: a faint tick.

### SH03 · OR · `@KF-2S` + `@ID_CLAIRE` `@ID_MAYA` + `@VOZ_MAYA` `@VOZ_CLAIRE` · 5 s
> (bloco de fala) Static side two-shot. Claire, on the left, stays focused on the model. Maya, on the right, chin on her hand, says with dry affection: "You know that's a tree, right?" Without looking up, Claire answers flatly: "I'm aware." (+ frase final)
*Se o lip-sync das duas falhar: gerar só a fala de Maya aqui; "I'm aware." no SH05.*

### SH04 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Over-the-shoulder medium shot of Maya, subtle handheld breathing. She tilts her head: "A tiny, plastic tree." (+ frase final)

### SH05 · OR · `@KF-C1` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static medium close-up. Claire keeps her eyes on the model: "It's blocking the entrance." (+ frase final)

### SH06 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Subtle handheld. Maya, deadpan and patient: "It's four millimeters tall." (+ frase final)

### SH07 · OR · `@KF-MINI` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static, low among the model trees. Claire, looming over the miniature city, narrows her eyes: "And somehow still in the wrong place." (+ frase final)

### SH08 · OR · `@KF-RACK` + `@ID_MAYA` + `@VOZ_MAYA` · 5 s
> (bloco de fala) Macro: in the sharp foreground, the tiny model tree slides about one centimeter and stops. Then the focus slowly shifts from the tree to Maya in the background, who says, unimpressed: "There. Civilization is saved." (+ frase final)
*Plano B: insert da árvore (SF) + o SH04 com a fala.*

### SH10 · OR · `@KF-C1` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static. Claire sits back slightly, studying the model with quiet satisfaction: "The entrance reads better now." (+ frase final)

### SH11 · OR · `@KF-2S` + ambos IDs + ambas vozes · 6 s
> (bloco de fala) Static side two-shot. Maya turns to Claire: "The entrance could win an award. You, on the other hand, need a weekend." Claire, still looking at the model, answers quickly: "I have a weekend." (+ frase final)

### SH12 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 5 s
> (bloco de fala) Subtle handheld. Maya counts on her fingers, amused: "You scheduled laundry for Saturday at nine and grocery shopping at eleven." (+ frase final)

### SH13 · OR · `@KF-C1` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static. Claire, dignified: "That's called having a life." (+ frase final)

### SH14 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Subtle handheld. Maya, a crooked smile: "That's called having a spreadsheet." (+ frase final)

### SH15 · SF · `KF-C1` · 4 s
> Static. Claire pointedly ignores her and lowers a clear acrylic cover over the model. Sound: acrylic settling.

### SH16 · SF · `KF-FOLDER-TOP` · 4 s
> Top-down, static. A hand slides the black folder into place beside the model and lets go. Sound: folder on the desk.

### SH17 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 6 s
> (bloco de fala) Subtle handheld. Maya, breezy, gesturing at the folder: "Tomorrow's presentation is ready. The redevelopment board, the community liaison, the documentary team—" (she is cut off mid-phrase). (+ frase final)

### SH18 · OR · `@KF-C3` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) A slow, noticeable push-in toward Claire's eyes as she looks up for the first time, a guarded flicker of attention: "The documentary team?" (+ frase final)

### SH19 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 7 s
> (bloco de fala) Subtle handheld. Maya shrugs with playful scorn: "Communications hired someone to document the restoration. Apparently, buildings need origin stories now." (+ frase final)

### SH20 · OR · `@KF-C1` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static. Claire, with quiet conviction: "Buildings have histories." (+ frase final)

### SH21 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Subtle handheld. Quick retort: "And apparently, histories need cameras." (+ frase final)

### SH22 · OR · `@KF-C2` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 5 s
> (bloco de fala) Static. Claire leafs through the open folder, dry and half-attentive: "As long as nobody films me pretending to enjoy a networking event." (+ frase final)

### SH23 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Subtle handheld. Maya, too innocent: "That's my entire marketing strategy." (+ frase final)

### SH24 · SF · `KF-EYES` · 4 s
> Static extreme close-up. Claire's eyes rise slowly over the edge of the folder and hold, unamused. No dialogue.

### SH25 · OR · `@KF-M1` + `@ID_MAYA` + `@VOZ_MAYA` · 4 s
> (bloco de fala) Subtle handheld. Maya, warm and firm: "Go home, Claire." (+ frase final)

### SH26 · OR · `@KF-2S` + ambos IDs + ambas vozes · 5 s
> (bloco de fala) Static two-shot. Claire, still holding the folder: "I am going home." Maya: "Without taking the building with you." (+ frase final)

### SH27 · OR · `@KF-C2` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> (bloco de fala) Static. Claire reluctantly sets the folder down on the desk: "Fine." (+ frase final)

### SH28 · OR · `@KF-2S` + ambos IDs + `@VOZ_MAYA` · 5 s
> (bloco de fala) Static two-shot. Claire immediately picks up her phone and looks at it, stands, takes the black trench coat from her chair over her arm and lifts her black bag. Maya says, exasperated and amused: "That's worse." (+ frase final)

### SH29 · OR · `@KF-DEEP` + ambos IDs + ambas vozes · 6 s
> (bloco de fala) Static deep-focus shot. In the background, Claire walks toward the elevators with the trench over her arm and says, without turning back: "Good night, Maya." In the foreground, Maya calls after her, warm and teasing: "Try doing something spontaneous!" (+ frase final)

### SH31 · OR · `@KF-TELE` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 5 s
> (bloco de fala) Static telephoto. At the elevator, Claire looks back over her shoulder, deadpan with a micro-smile: "I'll consider scheduling it." Then she steps into the opening elevator. Sound: elevator doors. (+ frase final)
**Nota para a montagem (V25):** escurecer o cabelo de Claire neste plano na correção de cor.

### SH32 · SF · `KF-M2` · 4 s
> Static close-up. Maya smiles fondly and shakes her head slightly. Sound: distant elevator chime.

---

## Ordem sugerida
1. **Teste: SH01, SH05 e SH03** (um movimento, uma fala, um plano a duas). Me mande os três.
2. Planos de uma personagem só (a maioria).
3. Planos a duas (SH11, SH26, SH28, SH29).
4. Os inserts sem fala (SH02, SH15, SH16, SH24, SH32).
