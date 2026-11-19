# Pacote ChatGPT — S01E02 · SC006 "The Man Who Remembered"

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha** e anexe as imagens R1–R8.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E02 "FAMILIAR STRANGERS" · SC006 "THE MAN WHO REMEMBERED"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Quando e onde:** terça à **tarde**, no set de entrevista da fábrica em restauração.
- **A entrevista:** Olivia Hayes, atrás da câmera, entrevista **Abel Ortiz, 74**, que teve uma loja de ferragens em frente ao prédio por 41 anos. **Claire Bennett** acompanha sentada ao lado, com um caderno, como representante do projeto.
- **A cena:** no meio da entrevista, Abel **reconhece Olivia** de sete anos atrás: "You're the girl with the camera." Claire percebe. Olivia não olha para Claire e segue para a próxima pergunta, calma demais.
- **Tom:** contido, um suspense pequeno. Abel é digno, seco e teimoso.
- **Visual:** Abel e Claire em quadros **parados**; Olivia com leve câmera na mão.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/ABEL_ORTIZ/abel-ortiz_identity-pack.png` | **Abel:** rosto, ângulos, figurino, óculos no bolso, mãos, cicatriz no polegar |
| **R2** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-SET-WS_V02.png` | **O set:** poltrona caramelo, caixote, painel de LED, câmera no tripé, carrinho do monitor, janelas altas |
| **R3** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | **Rosto e cor do cabelo de Claire** |
| **R4** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC003_KF-C3_V01.png` | **Claire hoje:** gola alta preta, pingente, cabelo castanho-escuro com franja |
| **R5** | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` | **Rosto de Olivia** (pinta) |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-O3_V01.png` | **Olivia hoje, atrás da câmera**, com o fone |
| **R7** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC001_KF-EXT_V02.png` | **A rua:** a fachada da fábrica e a **loja de velas** em frente |
| **R8** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-INS-MIC_V01.png` | **O microfone de lapela** preto |

## 3. Personagens (traços FIXOS + look de hoje)
**ABEL ORTIZ**, 74, porto-riquenho de Nova York.
- **Rosto:** igual a R1. Cabelo grisalho penteado com cuidado, **bigode grisalho curto**, olhos castanhos com rugas de riso, nariz marcado, pele morena clara; porte médio, levemente curvado, digno.
- **Look:**
  - **cardigã de lã verde-escuro** sobre **camisa azul-clara passada**, calça cinza e sapatos marrons engraxados;
  - **óculos de leitura no bolso da camisa**;
  - **microfone de lapela preto** preso na camisa (R8).
- **Mãos** grandes e gastas, com **uma pequena cicatriz num polegar**.
- **Não pode se parecer com nenhuma pessoa real.**

**CLAIRE BENNETT**, 35.
- **Rosto:** igual a R3. **Cabelo castanho-escuro, longo, ondulado, com franja cortina**; batom vinho.
- **Look:** **gola alta preta fina** com o **pingente vermelho-escuro por cima**, **calça taupe**, botas pretas, argolas douradas e **relógio no pulso ESQUERDO**.
- **Sem microfone**, **caderno e caneta** na mão. Sentada numa **cadeira dobrável preta**.

**OLIVIA HAYES**, 33.
- **Rosto:** igual a R5, com **UMA pinta pequena logo abaixo do lábio inferior, do LADO ESQUERDO dela**.
- **Look:** **suéter de tricô marrom**, **coque bagunçado** loiro-escuro e **fone de ouvido**; **SEM relógio**.
- Fica **atrás da câmera**, no tripé.

## 4. Cenário, eixos e luz
- **O set de R2, à TARDE:**
  - a mesma poltrona de couro caramelo, o caixote, o painel de LED **aceso** com luz suave, a câmera no tripé e o carrinho do monitor;
  - as janelas altas em arco atrás da poltrona.
- **Posições:**
  - **Abel na poltrona**, olhando para a **DIREITA** (para a câmera).
  - **A câmera e Olivia** à **direita** do quadro; Olivia olha para a **ESQUERDA** (o monitor e Abel).
  - **Claire** na cadeira dobrável **ao lado do carrinho do monitor**, a uns dois metros de Olivia. Para Abel, ela olha para a **ESQUERDA**; para Olivia, vira-se para a **DIREITA**.
- **Luz:** **tarde**. A luz das janelas se deslocou e ficou **mais quente, dourada e baixa**, entrando de lado; o LED dá uma luz principal suave em Abel. **Mais quente que a manhã de R2.**
- **Sem texto legível:** nem na vitrine da loja de velas, nem no caderno de Claire, nem no monitor.

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — Identidade de Abel em cena (aprovar o KF-A1 antes de tudo)
| ID | Refs | Prompt |
|---|---|---|
| **KF-A1** | R1, R2, R8 | Medium close-up, static: Abel, 74, the man from R1, seated in the caramel leather armchair from R2, looking toward the **RIGHT** at a camera just off-screen; dignified, dry, a man who fixed things all his life. Dark-green wool cardigan over a pressed light-blue shirt, reading glasses in the shirt pocket, a small black lavalier microphone clipped to the shirt. Tall arched factory windows behind him, warm low afternoon light from the side, a soft LED key light on his face. 16:9, 85mm. |
| **KF-SET-PM** | R2, R1, R4, R6, KF-A1 | The interview set from R2 in the **afternoon**: warmer, lower golden light from the windows, LED panel on. Abel seated in the armchair, facing right toward the camera. On the right, Olivia behind the camera on its tripod, with headphones. Beside the monitor cart, Claire on a black folding chair, a notebook on her knee, pen in hand, watching Abel. Static wide. 16:9, 28mm. |

### Etapa 2 — Abel
| ID | Refs | Prompt |
|---|---|---|
| **KF-A2** | KF-A1, R1 | Same framing as KF-A1: Abel turns in the armchair and points over his left shoulder toward the tall arched window behind him, proud, matter-of-fact. Same clothes, mic and light. 16:9, 85mm. |
| **KF-A3** | KF-A1, R1 | Same framing as KF-A1: Abel leans slightly to one side in the armchair, squinting **past** the camera at the person behind it, brow furrowed, the look of recognition: he has seen this woman before. Same clothes, mic and light. 16:9, 85mm. |
| **KF-INS-HANDS** | R1, KF-A1 | Close-up: Abel's big, weathered hands resting on the caramel leather armrest, a **small scar on one thumb**, the dark-green cardigan sleeve. Warm afternoon light. 16:9, 100mm. |
| **KF-WINDOW-SHOP** | R7, R2 | View through the tall arched multi-pane window of the factory, in warm afternoon light: across the quiet street, the **glass storefront of a small candle shop**, its window full of candles (as in R7), **no readable sign or text**. Slight dust on the glass. 16:9, 50mm. |

### Etapa 3 — Claire (aprovar o KF-C8; o C9 e o C10 são edições dele)
| ID | Refs | Prompt |
|---|---|---|
| **KF-C8** | R3, R4, R2 | Medium shot, static: Claire seated on a black folding chair beside the monitor cart, a notebook on her knee, writing, eyes toward the **LEFT** (Abel off-screen); composed, professional. Black turtleneck with the dark-red pendant on top, taupe trousers, watch on her LEFT wrist; dark-brown hair with curtain bangs, wine-red lipstick. No microphone. Warm afternoon light. 16:9, 50mm. |
| **KF-C9** | KF-C8 | **Editar o KF-C8:** same image; Claire has stopped writing and lifts her eyes from the notebook toward the LEFT, alert, caught by what she just heard. |
| **KF-C10** | KF-C8 | **Editar o KF-C8:** same image; Claire turns her head toward the **RIGHT** (Olivia off-screen), the pen still, studying her: serious, measuring, a quiet question in her eyes. |

### Etapa 4 — Olivia
| ID | Refs | Prompt |
|---|---|---|
| **KF-O7** | R5, R6, R2 | Medium close-up, subtle handheld: Olivia behind the camera on its tripod, headphones on, eyes toward the **LEFT** on the camera's monitor and the man beyond it; her face very still and controlled, too calm, jaw slightly set; she does **not** look at the woman sitting to her right. Brown knit sweater, messy dark-blond bun, ONE beauty mark below her lower lip on her LEFT side, no wristwatch. Warm afternoon light. 16:9, 85mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto (Abel = R1; Claire = R3; Olivia = R5) ✔/✖ · cabelo (Claire castanho-escuro) ✔/✖ · figurino ✔/✖ · microfone (só em Abel) ✔/✖ · óculos no bolso e cicatriz (Abel) ✔/✖ · pinta (Olivia, UMA) ✔/✖ · relógio (Claire no esquerdo; Olivia sem) ✔/✖ · luz de TARDE (mais quente) ✔/✖ · direção do olhar ✔/✖ · sem texto legível ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **Abel:**
  - rosto igual a R1, bigode grisalho;
  - cardigã **verde-escuro** (não o verde-oliva), camisa azul-clara, óculos no bolso, microfone;
  - olha para a **direita**;
  - **não lembra nenhuma pessoa real**.
- **Claire:**
  - rosto igual a R3, franja, gola alta com pingente, calça taupe;
  - sem microfone, caderno na mão;
  - Abel à **esquerda** e Olivia à **direita**.
- **Olivia:** rosto igual a R5, uma pinta, suéter marrom, fone, sem relógio; olha para a **esquerda**, **nunca** para Claire.
- **Luz:** tarde, **mais quente e baixa que a manhã**, com o LED aceso.
- **O mesmo set** de R2: a poltrona, o caixote e as janelas.
