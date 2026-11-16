# Pacote ChatGPT — S01E01 · SC008

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha**, com as imagens R1–R6 anexadas.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E01 · SC008 — "THE FIRST RULE"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Antes:** Claire Bennett, arquiteta, descobriu que a ex, Olivia Hayes, é a fotógrafa do documentário sobre o projeto dela. Na cena anterior, Claire impôs regras de trabalho: nada pessoal, nenhuma surpresa.
- **Esta cena:** **sexta-feira, fim de tarde**, na **mesma sala de reuniões de vidro**. Olivia fotografa a maquete do projeto; Claire trabalha no laptop fingindo não notar. Claire acaba ajudando ("the light is better from the west"); as duas quase riem juntas. **É a primeira cena leve e calorosa entre elas.**
- **Visual:** Claire em quadros **parados**; Olivia com leve câmera na mão.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | Rosto e **cor do cabelo** de Claire (é a referência que manda) |
| **R2** | `06_GENERATED_ASSETS/IMAGES/S01E01_SC007_KF-C2_V01.png` | **O look de Claire** (igual ao da cena anterior) |
| **R3** | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` | **Rosto de Olivia aprovado** (é a referência que manda), pinta |
| **R4** | `06_GENERATED_ASSETS/IMAGES/S01E01_SC007_KF-O1_V02.png` | **O look de Olivia** (coque bagunçado, camisa verde-oliva) |
| **R5** | `06_GENERATED_ASSETS/IMAGES/S01E01_SC007_KF-2S_V03.png` | **A sala**: mesa longa, maquete branca, janelas, tela desligada |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E01_SC006_KF-PLATE-ROOM_V01.png` | A sala vazia: a porta de vidro de um lado, as janelas do outro |

⚠️ **R2, R4, R5 e R6 são de manhã nublada. Esta cena é de FIM DE TARDE COM SOL** (ver seção 4). Use essas imagens para rosto, roupa e sala, **não para a luz**.

## 3. Personagens (traços FIXOS + look da cena)
**CLAIRE BENNETT**, 35.
- Rosto igual a R1; **cabelo castanho-escuro, longo, ondulado, com franja** (nunca acobreado); sobrancelhas fortes; **batom vinho**.
- **Look (igual a R2):** camisa de seda preta, calça pantalona creme; argolas douradas; colar duplo dourado (pingente vermelho-escuro); **relógio de mostrador branco e pulseira preta no PULSO ESQUERDO**.
- **Sentada na cabeceira da mesa** (do lado da tela desligada), com um **laptop prateado** aberto.

**OLIVIA HAYES**, 33.
- Rosto igual a R3; olhos verde-avelã; sardas leves; **pinta logo abaixo do lábio inferior, do LADO ESQUERDO dela** (à direita da imagem quando ela olha para a câmera).
- **Cabelo loiro-escuro, ondulado, em coque bagunçado**, mechas soltas (como R4).
- **Look (como R4):** camisa utilitária **verde-oliva aberta, mangas dobradas até o cotovelo**, top preto, calça cargo escura, coturno; argolas pequenas, colares finos em camadas, anéis finos.
- **Uma câmera fotográfica profissional (corpo preto, sem marca visível)** nas mãos. A **bolsa de câmera** de lona verde com couro fica numa cadeira.
- **Tatuagem pequena de câmera fotográfica, em traço fino, no antebraço interno ESQUERDO.**

## 4. Cenário, eixos e luz
- **A mesma sala de R5/R6:** mesa longa de madeira, cadeiras pretas, **maquete branca no centro**, tela na parede **desligada (preta)**, **porta de vidro de um lado e janelas do piso ao teto do outro**.
- **As janelas são o OESTE. LUZ: FIM DE TARDE, o céu nublado abriu: sol baixo, dourado e quente entrando pelas janelas, sombras longas na mesa, nuvens se abrindo no céu.** A mesma luz em todas as imagens.
- **Olivia em dois lados:**
  - **Posição A, lado da PORTA**, de costas para a porta: fotografa a maquete contra a janela, que fica em contraluz.
  - **Posição B, lado da JANELA**, com a luz quente batendo de lado nela e na maquete.
- **Eixo (muito importante):**
  - Com Olivia em A: **Claire olha para a ESQUERDA do quadro**; **Olivia olha para a DIREITA**.
  - Com Olivia em B: **Claire olha para a DIREITA do quadro**; **Olivia olha para a ESQUERDA**.
- **Sem texto legível** (tela do laptop clara e ilegível; câmera sem marca).

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — A luz da sala (aprovar antes de seguir)
**KF-WS** · R5, R6, R1–R4
> Wide shot of the glass conference room from R5 in late-afternoon light: the overcast sky has broken, a low warm golden sun comes through the floor-to-ceiling windows, long shadows across the long wooden table, the white architectural model at the center, the presentation screen switched off (black). Claire (R1/R2) sits at the head of the table near the black screen with an open silver laptop. Olivia (R3/R4) stands on the door side of the table, opposite the windows, photographing the model with a black professional camera; the model is backlit against the bright windows. A canvas camera bag on a chair. 16:9, 24mm, photorealistic.

### Etapa 2 — Olivia
| ID | Refs | Prompt |
|---|---|---|
| **KF-O1** | R3, R4, KF-WS | Medium shot, position A: Olivia stands on the door side of the conference table holding a black professional camera at chest height, looking toward the RIGHT side of the frame with a calm, amused expression. Messy dark-blond bun, open olive-green utility shirt with sleeves rolled to the elbow over a black top, thin layered necklaces, a small beauty mark just below her lower lip on her LEFT side. Warm late-afternoon window light from the right of frame. 16:9, 50mm. |
| **KF-O-LOW** | R3, R4, KF-WS | Olivia crouches at the edge of the table on the door side, photographing the white model from a low angle; the model is backlit by the bright golden windows behind it; her face partly visible behind the camera. 16:9, 35mm. |
| **KF-O2** | R3, R4, KF-WS | Medium shot, position B: Olivia stands by the windows, warm low sunlight hitting her from the side, camera lowered in her hands, looking toward the LEFT side of the frame, a knowing half-smile. Same look; beauty mark below her lower lip on her LEFT side. 16:9, 50mm. |
| **KF-O3** | R3, R4 | Close-up of Olivia (same side and same light as KF-O2), looking toward the LEFT side of the frame, warm and teasing; golden sunlight on her face; messy bun; beauty mark on her LEFT side. 16:9, 85mm. |
| **KF-INS-CAM** | R4 | Close-up of Olivia's hands holding a black professional camera (no visible brand), finger on the shutter button; thin gold rings; olive-green rolled sleeve; on her inner LEFT forearm a small fine-line tattoo of a vintage camera. Warm late-afternoon light. 16:9, 85mm. |

### Etapa 3 — Claire, a maquete e o plano a duas
| ID | Refs | Prompt |
|---|---|---|
| **KF-C1** | R1, R2, KF-WS | Medium shot, static: Claire seated at the head of the conference table with an open silver laptop (screen not readable), eyes down on the screen but glancing toward the LEFT side of the frame, pretending not to notice. Black silk blouse, wine-red lipstick, dark-brown long wavy hair with curtain bangs, white-dial watch on her LEFT wrist. Warm late-afternoon light. 16:9, 50mm. |
| **KF-C2** | R1, R2, KF-WS | Same seat, medium shot, static: Claire looks up toward the RIGHT side of the frame, toward the windows; warm golden sunlight on her face; composed, a trace of reluctant amusement. 16:9, 50mm. |
| **KF-C3** | R1, R2 | Close-up of Claire (same side and same light as KF-C2), looking toward the RIGHT side of the frame, suppressing a laugh, the corner of her mouth almost giving way. Wine-red lipstick, bangs, gold hoops. 16:9, 85mm. |
| **KF-INS-MODEL** | R5 | Close-up of the white architectural model on the wooden table, lit by low warm golden sunlight from the side: long soft shadows, glowing white surfaces, tiny model trees. 16:9, 85mm. |
| **KF-2S** | KF-C2, KF-O2, R5 | Two-shot across the conference table in golden late-afternoon light, the white model between them: Claire seated on the LEFT at the head of the table with her laptop, looking right; Olivia standing on the RIGHT by the windows with her camera, looking left. Neither speaks; a quiet, familiar moment. 16:9, 35mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
Depois de **cada** imagem, antes de eu aprovar:
`[ID] · rosto ✔/✖ · cabelo ✔/✖ · pinta (Olivia) ✔/✖ · figurino ✔/✖ · relógio no pulso esquerdo (Claire) ✔/✖ · lado e direção do olhar ✔/✖ · luz (fim de tarde com sol, a mesma em todas) ✔/✖ · tela desligada ✔/✖ · texto ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **Claire:** rosto igual a R1; franja; batom vinho; seda preta; relógio no pulso esquerdo; sentada com o laptop.
- **Olivia:** rosto igual a R3; **pinta do lado esquerdo dela**; coque; verde-oliva com mangas dobradas; câmera nas mãos; **tatuagem no antebraço interno esquerdo** (no insert).
- **Eixo:** C1 olha para a esquerda; C2 e C3 para a direita; O1 para a direita; O2 e O3 para a esquerda.
- A mesma sala; **sol baixo e quente pelas janelas** em todas as imagens; tela desligada; nenhum texto legível.
