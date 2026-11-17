# Pacote ChatGPT — S01E02 · SC002 + SC003

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha**, com as imagens R1–R9 anexadas.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E02 "FAMILIAR STRANGERS" · SC002 "LIGHTS" + SC003 "ON THE RECORD"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Terça de manhã, na fábrica em restauração.** Olivia Hayes, documentarista e ex de Claire Bennett, vai entrevistar Claire para o documentário sobre o projeto dela.
- **SC002:** Olivia monta o set. Muda a luz para o lado que Claire prefere, deixa um copo d'água antes de Claire pedir e prende o microfone de lapela na gola dela. **Um segundo perto demais.**
- **SC003:** a entrevista. Claire responde para a câmera; Olivia fica **atrás da câmera**. Maya e June assistem atrás do monitor.
- **Visual:** Claire em quadros **parados**; Olivia, Maya e June com leve câmera na mão.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | **Rosto e cor do cabelo de Claire** (a referência que manda) |
| **R2** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC001_KF-C1_V01.png` | **Claire hoje:** gola alta, pingente, luz da fábrica (aqui **sem o capacete**) |
| **R3** | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` | **Rosto de Olivia** (pinta) |
| **R4** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC001_KF-O1_V01.png` | **Olivia hoje:** suéter marrom, coque, sem capacete |
| **R5** | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` | Rosto de Maya |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC001_KF-MJ_V02.png` | **Maya e June hoje**, as duas de creme |
| **R7** | `02_CHARACTERS/JUNE_PARK/june_ref-SC005_KF-J1.png` | Rosto de June |
| **R8** | `03_LOCATIONS/FABRICA_RESTAURACAO/fabrica_ref-set-entrevista.png` | **O set de entrevista:** poltrona de couro caramelo, caixote, refletor, câmera no tripé, janelas altas |
| **R9** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC001_KF-INT-WS_V02.png` | O salão da fábrica e a luz desta manhã |

## 3. Personagens (traços FIXOS + look de hoje)
**CLAIRE BENNETT**, 35.
- Rosto igual a R1; **cabelo castanho-escuro (nunca acobreado), longo, ondulado, com franja cortina**; **batom vinho**.
- **Look (R2):** **gola alta preta fina** com o **pingente vermelho-escuro por cima**, calça taupe, cinto preto, botas pretas; argolas douradas; **relógio de mostrador branco e pulseira preta no PULSO ESQUERDO**; **unhas naturais**, sem esmalte.
- **No set, SEM capacete.** O capacete branco fica no chão, ao lado da poltrona.
- **Na SC003:** um **microfone de lapela preto, pequeno, preso na borda da gola alta**.

**OLIVIA HAYES**, 33.
- Rosto igual a R3; **UMA pinta pequena logo abaixo do lábio inferior, do LADO ESQUERDO dela** (à direita da imagem quando ela olha para a câmera).
- **Look (R4):** suéter de tricô marrom de ombro caído, jeans, coque bagunçado loiro-escuro, argolas pequenas, colares finos; **tatuagem pequena de câmera no antebraço interno ESQUERDO**. **Sem capacete** no set.

**MAYA e JUNE** (R5, R6, R7): Maya com cachos castanho-escuros e acobreados na altura do queixo, de creme; June com cabelo liso na clavícula, overshirt creme, crachá, prancheta. **Sem capacetes** no set.

## 4. Cenário, eixos e luz
- **O set (R8)**, junto às janelas altas em arco da fábrica: **poltrona de couro caramelo**; **caixote de madeira** ao lado, como mesinha; um **refletor** de LED num tripé; a **câmera de cinema num tripé**, com um **monitor** pequeno; tijolo aparente, colunas de ferro.
- **Posições:**
  - **Claire sentada na poltrona.**
  - **A câmera e Olivia** ficam à frente dela, um pouco **à direita**.
  - **Maya e June** ficam atrás de Olivia, junto ao monitor.
- **Eixo:** **Claire olha sempre para a DIREITA do quadro** (para Olivia, ao lado da lente). **Olivia, Maya e June olham para a ESQUERDA.**
- **Luz:** a manhã clara de outono pelas janelas (como R9) e a luz suave do refletor no rosto de Claire.
- **Texto:** nenhum texto legível. Monitor e câmera sem marcas legíveis.

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — O set e Claire na poltrona (aprovar o KF-C1 antes de seguir)
| ID | Refs | Prompt |
|---|---|---|
| **KF-SET-WS** | R8, R9, R2, R4 | Wide shot of the interview set from R8 by the tall arched windows of the old brick factory, clear morning light: Claire (R1/R2, no hard hat; her white hard hat on the floor beside the chair) sitting down in the caramel leather armchair; Olivia (R3/R4) carrying the LED light on its stand from Claire's right side toward her left side; the cinema camera on a tripod and a small monitor in the foreground right. 16:9, 28mm, photorealistic. |
| **KF-C1** | R1, R2, R8 | Medium shot, static: Claire seated in the caramel leather armchair by the tall windows, **no hard hat**, looking toward the **RIGHT** side of the frame, composed and slightly wary; a small wooden crate beside her. Black turtleneck with the dark-red pendant, wine-red lipstick, dark-brown hair with curtain bangs, watch on her LEFT wrist. Soft key light on her face, morning light from the windows. 16:9, 50mm. |
| **KF-C2** | R1, R2, KF-C1 | Close-up of Claire seated (same light), looking **up and to the RIGHT** at someone standing very near her, holding still, a held breath. 16:9, 85mm. |
| **KF-C3** | R1, R2, KF-C1 | **The interview frame:** medium close-up of Claire in the armchair, a small black lavalier microphone clipped to the edge of her turtleneck, looking just beside the lens toward the **RIGHT**; soft key light, the tall window softly out of focus behind her. Static, composed, controlled. 16:9, 50mm. |
| **KF-C4** | KF-C3 | Same as KF-C3 but a **close-up**: her face fills more of the frame; the control in her eyes starting to crack. 16:9, 85mm. |

### Etapa 2 — Olivia
| ID | Refs | Prompt |
|---|---|---|
| **KF-O1** | R3, R4, R8 | Medium shot: Olivia adjusting the LED light on its stand, looking toward the **LEFT** side of the frame (at Claire off-screen), focused and quietly amused; the brick wall and tall windows behind her. No hard hat. ONE beauty mark below her lower lip on her LEFT side. 16:9, 50mm. |
| **KF-O2** | R3, R4, R8 | Medium shot: Olivia behind the cinema camera on its tripod, one eye near the small monitor, then glancing toward the **LEFT**; brown knit sweater, messy bun. 16:9, 50mm. |
| **KF-O3** | KF-O2 | Same position behind the camera, Olivia **wearing headphones**, perfectly still, watching Claire off-screen to the **LEFT**; quiet, attentive, unreadable. 16:9, 50mm. |

### Etapa 3 — Inserts e planos a duas
| ID | Refs | Prompt |
|---|---|---|
| **KF-INS-WATER** | R4, R8 | Close-up: Olivia's hand (thin gold rings, the small fine-line camera tattoo on her inner LEFT forearm, brown knit sleeve) setting a glass of water on the small wooden crate beside the caramel armchair. Morning light. 16:9, 85mm. |
| **KF-INS-MON-A** | KF-C1 | Close-up of the small monitor on the camera rig: on its screen, Claire seated in the armchair, and **an iron column behind her looking as if it grows out of the top of her head**. No readable text on the monitor. 16:9, 85mm. |
| **KF-INS-MON-B** | KF-INS-MON-A | Same monitor, same framing: now the column is **out of the frame** on the screen; Claire well composed. |
| **KF-2S-MIC** | KF-C1, KF-O1 | Two-shot: Claire seated in the armchair on the LEFT; Olivia standing on the RIGHT, **stopped an arm's length away**, a small black lavalier microphone in her hand, asking permission with her eyes. Static. 16:9, 35mm. |
| **KF-INS-MIC** | KF-C1, R4 | Close-up: Olivia's fingers clipping a small black lavalier microphone to the edge of Claire's black turtleneck, near the pendant; careful, quick, professional. 16:9, 100mm. |
| **KF-2S-CLOSE** | KF-2S-MIC | Close two-shot: Olivia leaning in, Claire seated, their faces very close for one second; neither moves. Static, shallow depth of field, soft key light. 16:9, 85mm. |
| **KF-INS-REC** | R8 | Close-up of the cinema camera body on the tripod: a small **red recording light** glowing. No readable brand. 16:9, 100mm. |
| **KF-MJ2** | R5, R6, R7 | Medium two-shot: Maya and June standing side by side behind the small monitor, **arms folded identically**, both in cream, watching toward the **LEFT**; no hard hats. Factory background softly out of focus. 16:9, 50mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto ✔/✖ · cabelo (Claire castanho-escuro) ✔/✖ · pinta (Olivia, UMA) ✔/✖ · figurino (sem capacetes no set) ✔/✖ · relógio no pulso esquerdo (Claire) ✔/✖ · unhas naturais ✔/✖ · direção do olhar ✔/✖ · luz ✔/✖ · sem texto ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **Claire:** rosto igual a R1; cabelo castanho-escuro com franja; batom vinho; gola alta preta com o pingente; relógio no pulso esquerdo; **sem capacete**; olha para a **direita**; **microfone na gola só em C3 e C4**.
- **Olivia:** rosto igual a R3; **uma pinta**; coque; suéter marrom; tatuagem nos inserts; olha para a **esquerda**; **de fone só no O3**.
- **Maya e June:** de creme, braços cruzados idênticos, sem capacete.
- O set igual a R8; luz da manhã; monitor com a **coluna na cabeça (A)** e **fora (B)**.
