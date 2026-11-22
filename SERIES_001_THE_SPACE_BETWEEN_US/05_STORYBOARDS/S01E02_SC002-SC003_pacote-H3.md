# Pacote de geração no H3 — S01E02 · SC002 + SC003 "Lights / On the Record"

**Plataforma:** buzzy.now · **Modelo:** MiniMax-H3 · **Data:** 2026-11-18 · **Blocos de voz revistos:** 2026-11-19 (V64, aplicando a lição da V62) · **Emoção revista:** 2026-11-22 (V70, regra do amor que não acabou)
**Base:** decupagem V01 (APROVADA, N33) + 16 keyframes aprovados (V58) · roteiro V1.2 · animatic `07_EDITING/S01E02_SC002-SC003_animatic_V01.mp4` (2:01) · storyboard `05_STORYBOARDS/S01E02_SC002-SC003_storyboard_V01.jpg`

## Regras destas cenas
1. **16:9**; 480p para teste, a maior resolução na versão final; salvar como `S01E02_SC002_SH##_V##.mp4` e `S01E02_SC003_SH##_V##.mp4`.
2. **Câmera (P-15):** Claire **parada**; Olivia, Maya e June com **leve respiração de câmera na mão**. **Um único avanço lento:** SC003 SH09 (N33).
3. **Vozes:** Claire com `@VOZ_CLAIRE` e Maya com `@VOZ_MAYA` (método A). **Olivia e June sem referência**: voz descrita no prompt, conversão na edição.
4. **Uma personagem falando por geração.**
5. **SC003, Olivia só como voz (O.S.):**
   - Os planos de Claire geram **só a resposta dela**.
   - As perguntas de Olivia saem de **planos-fonte** gerados com o KF-O3 e com o bloco de Olivia; use **só o áudio**, encaixado antes de cada resposta.
6. **Eixo:** Claire olha para a **direita**; Olivia, Maya e June para a **esquerda**.
7. **Texto do monitor** (STBY, timecode) já está na imagem; não alterar.

## ⚠️ Dois ajustes de continuidade (faça antes de gerar)
1. **O copo d'água:** depois do SH08 o copo está no caixote, mas o **KF-C1 tem o caixote vazio**. Para SH09, SH12 e SH15, use um **KF-C1-B**, que é o mesmo C1 com o copo no caixote. Feito por composição (o ChatGPT gerou outra imagem em vez de editar): `S01E02_SC002_KF-C1-B_V01.png`.
2. **O microfone:** depois do SH18 o microfone está na gola. O **SH21 ("Something.")** usa o **KF-C3** (com microfone), e não o C1.

## Arquivos
| Etiqueta | Arquivo |
|---|---|
| `@ID_CLAIRE` | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` |
| `@ID_MAYA` | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` |
| `@ID_OLIVIA` | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` |
| `@ID_JUNE` | `02_CHARACTERS/JUNE_PARK/june_ref-SC005_KF-J1.png` |
| `@VOZ_CLAIRE` | `06_GENERATED_ASSETS/VOICES/claire_bennett_voice-ref_v02.wav` |
| `@VOZ_MAYA` | `06_GENERATED_ASSETS/VOICES/maya_reed_voice-ref_v02.wav` |
| `@KF-…` SC002 | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-…`: SET-WS V02 · C1 V01 · **C1-B V01** (composição: o copo do INS-WATER sobre o caixote do C1) · C2 V01 · O1 V02 · O2 V01 · O3 V01 · INS-WATER V02 · INS-MON-A V02 · INS-MON-B V02 · 2S-MIC V02 · INS-MIC V01 · 2S-CLOSE V01 |
| `@KF-…` SC003 | `06_GENERATED_ASSETS/IMAGES/S01E02_SC003_KF-…`: C3 V01 · C4 V01 · INS-REC V01 · MJ2 V02 |

**Bloco de Claire (OR):** *Use @KF-… as the opening frame and composition. Keep @ID_CLAIRE's face. Claire speaks in the voice of @VOZ_CLAIRE. Story: she is being filmed by the woman she still loves and has not forgiven. Olivia's closeness (the light on her preferred side, the water she didn't ask for, the microphone) undoes her a little each time, and dryness is the only armor she has. In the interview her answers start rehearsed and fluent; when the questions turn personal the control cracks: a hesitation, a softer voice, eyes that go to Olivia and glisten, no tear. Static camera.*

**Bloco de Olivia (OR):** *Use @KF-… as the opening frame and composition. Keep @ID_OLIVIA's face (messy bun today). Olivia speaks in a warm, medium-low, slightly husky American voice. Story: she still loves Claire and knows her better than anyone; every small gesture is a way of taking care of her without saying so. Soft and unhurried, a breath before she speaks to her, her eyes lingering on Claire; behind the camera her questions are tender and deliberate, and the personal ones cost her. Never teasing for its own sake. Subtle handheld camera breathing.*

**Bloco de Maya (OR):** *Use @KF-… as the opening frame. Keep @ID_MAYA's face. Maya speaks in the voice of @VOZ_MAYA: a dry whisper with comic timing, a tiny pause before the punchline; underneath, she is watching her best friend unravel on camera, and the joke is how she copes. No laughing, at most a dry half-smile. Subtle handheld.*

**Bloco de June (OR):** *Use @KF-… as the opening frame. Keep @ID_JUNE's identity. June whispers in a dry, medium-low American voice with sharp comic timing. Her FACE is deadpan, but her VOICE is not flat: a tiny pause before the punchline and a light, ironic stress on the key word. Subtle handheld.*

**Subtexto obrigatório (V70), vale para todo plano de Claire e Olivia:** *Seven years ago Olivia left Claire without explaining. They never stopped loving each other, and the hurt never closed. Under every exchange between them there is a love that did not end and a wound that did not heal: no line between them is neutral. Olivia looks at Claire a beat too long and looks away when it hurts; her smiles break halfway; she breathes before she speaks to her. Claire's control is the armor of someone who still feels: her eyes betray her, holding Olivia's gaze and then fleeing; her voice drops and catches on anything personal. Tears scale: (1) eyes glistening, no tear — the default for subtext; (2) one contained tear she tries to hide — only where marked; (3) open crying — not in this episode.*

**Frase final de todo prompt:** *Clear autumn morning light through the tall arched windows of the old brick factory, soft LED key light on Claire. Claire: dark-brown wavy hair with curtain bangs, wine-red lipstick, black turtleneck with dark-red pendant, taupe trousers, watch on her LEFT wrist, seated in the caramel leather armchair with a black metal frame. Olivia: messy dark-blond bun, brown knit sweater, jeans, no wristwatch, camera tattoo on her inner left forearm, one beauty mark below her lower lip on her left side. Maya and June in cream. Keep all on-screen text as it is. No music.*

## Planos — SC002
| Plano | Modo | Keyframe | Fala | Prompt |
|---|---|---|---|---|
| SH01 | SF | SET-WS | — | Static wide shot. Claire sits down in the armchair; Olivia carries the LED panel from Claire's right side to her left. |
| SH02 | OR | C1 + Claire | CLAIRE "What are you doing?" | (bloco Claire) Suspicious: "What are you doing?" |
| SH03 | OR | O1 + Olivia | OLIVIA "Moving the light." | (bloco Olivia) Adjusting the panel, not looking: "Moving the light." |
| SH04 | OR | C1 + Claire | CLAIRE "I can see that." | (bloco Claire) "I can see that." |
| SH05 | OR | O1 + Olivia | OLIVIA "You have a preferred side." | (bloco Olivia) "You have a preferred side." |
| SH06 | OR | C1 + Claire | CLAIRE "I don't have a good side." | (bloco Claire) "I don't have a good side." |
| SH07 | OR | O1 + Olivia | OLIVIA "I said preferred." | (bloco Olivia) A small smile that holds more than it should; softly: "I said preferred." |
| SH08 | SF | INS-WATER | — | Close-up. Olivia's hand sets the glass of water on the crate and withdraws. |
| SH09 | SF | **C1-B** | — | Static. Claire looks at the glass; she hadn't asked. Something soft flickers in her eyes, the memory of being known; she picks it up and drinks anyway. |
| SH10 | SF | O2 | — | Subtle handheld. Olivia checks the frame on the camera. |
| SH11 | SF | INS-MON-A | — | Static. On the monitor, the column grows out of Claire's head. |
| SH12 | OR | **C1-B** + Claire | CLAIRE "The column is cutting through my head." | (bloco Claire) Dry, with a hint of irritation: "The column is cutting through my head." |
| SH13 | OR | O2 + Olivia | OLIVIA "I was just about to fix that." | (bloco Olivia) "I was just about to fix that." |
| SH14 | SF | INS-MON-A → INS-MON-B | — | Static. The image on the monitor slides a few inches; the column leaves the frame. (Start frame A, end frame B.) |
| SH15 | OR | **C1-B** + Claire | CLAIRE "Of course you were." | (bloco Claire) "Of course you were." |
| SH16 | OR | 2S-MIC + Olivia | OLIVIA "May I?" | (bloco Olivia) Stopped an arm's length away, lavalier in hand, barely above a whisper, her eyes on Claire's: "May I?" |
| SH17 | OR | C2 + Claire | CLAIRE "Yes." | (bloco Claire) A long beat; her eyes meet Olivia's and hold; then, quietly, almost a breath: "Yes." |
| SH18 | SF | INS-MIC | — | Olivia clips the microphone to the edge of the turtleneck and runs the cable under the knit; Claire watches her. |
| SH19 | SF | 2S-CLOSE | — | Static. Their faces very close for two seconds; both breathe; neither moves; the seven years are in their eyes. Room tone only. |
| SH20 | OR | O3 + Olivia | OLIVIA "Say something." | (bloco Olivia) Back behind the camera, headphones on: "Say something." |
| SH21 | OR | **C3** + Claire | CLAIRE "Something." | (bloco Claire) Deliberately flat, a tiny defiant pause before it: "Something." |
| SH22 | OR | O3 + Olivia | OLIVIA "Perfect." | (bloco Olivia) Checking the headphones: "Perfect." |

## Planos — SC003
| Plano | Modo | Keyframe | Fala (Claire em quadro) | Prompt |
|---|---|---|---|---|
| SH01 | SF | INS-REC | — | Static. The red recording light on the camera body turns on. Sound: soft beep. |
| SH02 | SF | MJ2 | — | Subtle handheld. Maya and June stand behind the monitor, arms folded identically, watching. |
| SH03 | OR | C3 + Claire | "Restoration is about deciding what deserves to stay." | (bloco Claire) Perfectly rehearsed, four seconds: "Restoration is about deciding what deserves to stay." |
| SH04 | OR | C3 + Claire | "The structure dates from 1928. Load-bearing brick, cast-iron columns, original timber floors on the upper levels. Our approach is to preserve the envelope and adapt the interior for community use." | (bloco Claire) Fluent, technical. **Generate in two parts**; cut at "Our approach…". |
| SH05 | OR | C3 + Claire | "We keep what's structurally sound and historically significant. We let go of what can't be saved." | (bloco Claire) Still in control. |
| SH06 | OR | C3 + Claire | "You test it." | (bloco Claire) Half a second of hesitation, then: "You test it." |
| SH07 | SF | MJ2 | — | Subtle handheld. Maya slowly turns her head toward June; June does not turn hers. |
| SH08 | OR | C3 + Claire | "Sometimes they're just abandoned. Sometimes someone keeps them." | (bloco Claire) Carefully. |
| SH09 | OR | C4 + Claire | "Here... some structures look intact from the outside. You don't know what's damaged until you open the walls." | (bloco Claire) **Very slow push-in** (about 10%). She says it before deciding to; her eyes go past the camera to Olivia and glisten: "Here... some structures look intact from the outside. You don't know what's damaged until you open the walls." |
| SH10 | SF | C4 | — | Static. Silence. Claire hears herself. |
| SH11 | SF | O3 | — | Subtle handheld. Olivia behind the camera, perfectly still, watching Claire; her eyes glisten; she understands what was just said. |
| SH12 | OR | C3 + Claire | "I'd like to do that again." … "All of it." | (bloco Claire) Composure back: "I'd like to do that again." A beat. "All of it." |
| SH13 | OR | MJ2 + Maya | MAYA "Is this a documentary or a deposition?" | (bloco Maya) Whispering to June. |
| SH14 | OR | MJ2 + June | JUNE "Yes." | (bloco June) Eyes on the monitor, whispering: "Yes." |
| SH15 | SF | C3 | — | Static. Claire straightens, ready. |
| SH16 | SF | C4 | — | Static. Claire looks past the camera, straight at Olivia. |
| SH17 | OR | C4 + Claire | "Next question." | (bloco Claire) Her voice catches on the first word: "Next question." |
| SH18 | SF | C4 | — | Static. A beat; she holds the look. |
| SH19 | OR | C4 + Claire | "Then we're done." | (bloco Claire) Quietly final, eyes glistening, not looking away: "Then we're done." |

## Áudio O.S. de Olivia (planos-fonte, só o áudio)
Gere com **KF-O3 + bloco de Olivia**, uma frase por geração, e encaixe antes da resposta de Claire:
"What is restoration about?" (SH03) · "Tell me about this building." (SH04) · "What do you keep, and what do you let go?" (SH05) · "How do you know what can't be saved?" (SH06) · "What happens to the things people leave behind?" (SH08) · "Which is it here?" (SH09) · "Which part?" (SH12) · "Last question." (SH15) · "Why did you stay in New York?" (SH16) · "That was the last one." (SH18)

## Montagem

### Emoção e pausas (V70)
Antes de toda fala pessoal entre Claire e Olivia, **1–2 s de silêncio**. Não corte colado.
- **SC002 SH16–SH19:** 1,5 s antes do "May I?"; 1,5–2 s antes do "Yes."; o SH19 inteiro (2–3 s) em silêncio.
- **SC003 SH09–SH11:** depois do "Here...", 2 s de silêncio antes do corte para Olivia.
- **SH16–SH19:** 1,5 s antes de "Next question." e de "Then we're done."

### Montagem geral
- **SC002:** as réplicas de SH02–SH07 em 1,5–2 s; **SH19**, segure o plano inteiro (3 s), sem som além da sala.
- **SC003:** as perguntas de Olivia soam um pouco mais baixas e próximas do microfone da câmera; **SH09–SH10**, deixe o silêncio durar; **SH16–SH19**, sem pressa.
- **Som:** sem música. Eco da fábrica, poeira e o zumbido baixo do refletor.
- **Final:** CUT TO a SC004.
