# Pacote de geração no H3 — S01E02 · SC009 "Raw Footage"

**Plataforma:** buzzy.now · **Modelo:** MiniMax-H3 · **Data:** 2026-11-19 · **Emoção revista:** 2026-11-22 (V70, regra do amor que não acabou)
**Base:**
- decupagem V01 (APROVADA, N39) + 14 keyframes aprovados (V69) + o KF-RAIN da SC003 do piloto, reaproveitado;
- roteiro V1.2;
- animatic `07_EDITING/S01E02_SC009_animatic_V01.mp4` (1:07);
- storyboard `05_STORYBOARDS/S01E02_SC009_storyboard_V01.jpg`.

## Regras desta cena
1. **Formato:** 16:9; 480p para teste e a maior resolução na versão final. Salve como `S01E02_SC009_SH##_V##.mp4`.
2. **Câmera:**
   - Claire **parada** (P-15); **nenhum avanço de câmera**;
   - **o BROLL** tem leve câmera na mão, porque é a câmera de Olivia.
3. **Claire não fala em cena.** A voz dela só aparece **na tela**: a fala da entrevista (áudio da SC003 SH09) e o **riso** do BROLL (com `@VOZ_CLAIRE`).
4. **Telas:**
   - nos planos de tela (FOLDER, FOLDER-LAST, DELETE), **não deixe o H3 reescrever o texto**: no máximo um movimento de cursor;
   - a entrevista (SH05) e o BROLL na tela (SH11, SH16) são **compostos na edição** com os vídeos reais; o keyframe serve de guia.
5. **Eixo:** Claire olha para a **direita** (a tela) e, no C16, para a **esquerda** (a parede de fotos, atrás dela).
6. **Luz:** noite; a tela do iMac é a única luz forte no rosto, com uma luminária quente ao fundo. O BROLL é a manhã na fábrica.

## Arquivos
| Etiqueta | Arquivo |
|---|---|
| `@ID_CLAIRE` | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` |
| `@VOZ_CLAIRE` | `06_GENERATED_ASSETS/VOICES/claire_bennett_voice-ref_v02.wav` |
| KF-RAIN | `06_GENERATED_ASSETS/IMAGES/S01E01_SC003_KF-RAIN_V01.png` (reaproveitado do piloto) |
| `@KF-…` | `06_GENERATED_ASSETS/IMAGES/S01E02_SC009_KF-…`: STUDY-WS V01 · C14 V02 · C15 V01 · C16 V01 · C17 V02 · BROLL V03 · WALL V02 · INS-PHOTO V01 · INS-FOLDER V03 · INS-FOLDER-LAST V02 · INS-DELETE V01 · INS-SCREEN-INT V01 · INS-FREEZE V01 · INS-MOUSE V01 |
| Entrevista na tela | o vídeo gerado da **SC003 SH09** (`S01E02_SC003_SH09_V##.mp4`), com o áudio dele |

**Bloco de Claire, sem fala (SF):** *Keep @ID_CLAIRE's face. Story: alone at night, Claire sees herself the way Olivia still sees her (the same angle, the same laugh, seven years apart) and understands that Olivia never stopped looking at her that way, and that she never stopped loving her either. Silent, restrained, every emotion small and inside; her eyes fill when she compares the photo and the screen; one tear slips and she wipes it away quickly. She does not delete the file. She speaks slowly, about two words per second, with small pauses inside the sentence; never rushed. Static camera.*

**Bloco do BROLL (OR, riso):** *Use @KF-BROLL as the opening frame and composition. Keep @ID_CLAIRE's face. Documentary B-roll, subtle handheld, shot from a little distance. Someone off-screen to her right says something, inaudible and distant; Claire laughs fully and unguarded, in the voice of @VOZ_CLAIRE: a real, surprised, open laugh, head tilted back, completely unaware of the camera. Morning light in the old brick factory.*

**Subtexto obrigatório (V70), vale para todo plano de Claire e Olivia:** *Seven years ago Olivia left Claire without explaining. They never stopped loving each other, and the hurt never closed. Under every exchange between them there is a love that did not end and a wound that did not heal: no line between them is neutral. Olivia looks at Claire a beat too long and looks away when it hurts; her smiles break halfway; she breathes before she speaks to her. Claire's control is the armor of someone who still feels: her eyes betray her, holding Olivia's gaze and then fleeing; her voice drops and catches on anything personal. Tears scale: (1) eyes glistening, no tear — the default for subtext; (2) one contained tear she tries to hide — only where marked; (3) open crying — not in this episode.*

**Frase final de todo prompt (planos no ateliê):** *Night in Claire's study: the cool blue-white light of the iMac screen on her face, a low warm desk lamp behind, shelves in half-darkness. Claire: long dark-brown wavy hair with curtain bangs, the ends slightly damp, wine-red lipstick, black turtleneck with ONE dark-red pendant, white-dial watch with a black strap on her LEFT wrist, no rings. No music.*

## Planos
| Plano | Modo | Keyframe | Fala / som | Prompt |
|---|---|---|---|---|
| SH01 | SF | RAIN (piloto) | (chuva) | Static. Rain streams down the tall living-room windows; the city lights blur behind the glass. |
| SH02 | SF | STUDY-WS | (chuva abafada) | Static wide. Claire sits at the desk in the dark study, lit only by the iMac screen; she moves the mouse; behind her, the photo wall in half-darkness. |
| SH03 | SF | INS-FOLDER | — | Static close-up of the screen. The folder is open; the cursor moves slightly toward the first file. The text does not change. |
| SH04 | SF | C14 | — | (bloco Claire) She clicks and watches, controlled, tired. |
| SH05 | SF | INS-SCREEN-INT | CLAIRE (ON SCREEN): "You don't know what's damaged until you open the walls." | Static. On the screen, the interview plays. **In the edit: replace the screen with the SC003 SH09 video and its audio.** |
| SH06 | SF | C14 | — | (bloco Claire) A small wince; she looks away for a second and skips ahead. |
| SH07 | SF | INS-FOLDER-LAST | — | Static close-up. The cursor rests on the last file, B-ROLL_BREAK_03.mov. The text does not change. |
| SH08 | SF | C14 | — | (bloco Claire) A beat of curiosity; she clicks. |
| SH09 | OR | BROLL + Claire | (murmúrio de Maya; riso de Claire) | (bloco BROLL) Claire laughs fully at something off-screen, head tilted back. |
| SH10 | SF | C15 | — | (bloco Claire) She watches herself laugh; her guard drops; lips parted; she didn't know she was being filmed, and she understands who was looking. |
| SH11 | SF | INS-FREEZE | (o riso corta) | Static. She stops the video; the laugh freezes on the screen. **In the edit: the screen shows the last frame of SH09, frozen.** |
| SH12 | SF | C15 → C16 | — | (bloco Claire) Slowly, she turns her chair to the left, toward the photo wall behind her. (Start frame C15, end frame C16.) |
| SH13 | SF | WALL | — | Static. The photo wall in half-darkness; a very slow drift of light; the small old photo among the buildings. |
| SH14 | SF | INS-PHOTO | — | Static. The old photo in its frame: Claire at 28, no bangs, laughing. |
| SH15 | SF | C16 | — | (bloco Claire) She looks at the wall, very still; her eyes fill. |
| SH16 | SF | INS-FREEZE | — | Static. The frozen laugh on the screen. |
| SH17 | SF | INS-PHOTO | — | Static. The old photo again. |
| SH18 | SF | INS-DELETE | — | Static close-up. The right-click menu is open; "Delete" is highlighted. The text does not change. |
| SH19 | SF | INS-MOUSE | — | Static close-up. Her index finger rests on the mouse button; a tiny tension in the finger; it does not press. |
| SH20 | SF | C14 → C17 | (clique) | (bloco Claire) She switches off the screen; the cool light vanishes; in the dark, one tear slips and she wipes it away quickly. (Start frame C14, end frame C17.) |
| SH21 | — | preto | — | CUT TO BLACK. Cartela "END OF EPISODE 02", se a produção quiser. |

## Montagem

### Emoção e pausas (V70)
Antes de toda fala pessoal entre Claire e Olivia, **1–2 s de silêncio**. Não corte colado.
- **SH13–SH17:** a comparação parede, tela, parede sem pressa; deixe os olhos de Claire encherem no SH15.
- **SH20:** a lágrima no escuro, 1–1,5 s, antes do preto.

### Planos de reação e ritmo (V71)
- **Ritmo:** entre Claire e Olivia, **70–85 palavras por minuto** e **pausa típica de 1,5–2 s** entre as falas; nunca menos de 1 s. Só a comédia de Maya e June fica rápida.

### Montagem geral
- **Os planos somam 1:07**, e os silêncios levam a cena para perto do 1:30.
  - **SH09:** deixe o riso inteiro, 5–6 s. É a coisa mais livre que ouvimos de Claire na série.
  - **SH11:** **corte seco** do riso para o silêncio.
  - **SH13–SH17:** a comparação parede, tela, parede em ritmo crescente: 2 s, 2 s e 2 s. **O mesmo ângulo, o mesmo riso.**
  - **SH19:** segure o dedo parado mais do que parece confortável.
  - **SH20–SH21:** a tela apaga, 1 s no rosto escuro e então o preto.
- **Telas:** componha os vídeos reais (SC003 SH09 e SH09 desta cena) dentro do monitor. Confira se o player (barra e ícones) é o mesmo nos dois.
- **Som:**
  - sem música até o fim;
  - **SH01–SH02:** a chuva; no ateliê, abafada, com o zumbido baixo do iMac;
  - **SH05:** a entrevista; **SH09:** o eco da fábrica, Maya ao longe e o riso;
  - **SH18–SH20:** silêncio quase total, só o clique ao desligar;
  - **SH21:** no preto, se a produção quiser, a primeira nota da música de encerramento (pendente: decisões de música).
- **Final:** CUT TO BLACK. **END OF EPISODE 02.**
