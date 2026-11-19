# Pacote ChatGPT — S01E02 · SC009 "Raw Footage"

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha** e anexe as imagens R1–R7.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E02 "FAMILIAR STRANGERS" · SC009 "RAW FOOTAGE"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Quando e onde:** terça à **noite**, com chuva lá fora, no **ateliê** do apartamento de Claire Bennett (mesa com iMac, estantes e uma parede de fotos).
- **A cena:**
  - Claire revisa o material bruto da entrevista que deu de manhã para o documentário;
  - no último arquivo há um plano que a fotógrafa (Olivia) fez dela no intervalo, sem que ela soubesse: **Claire rindo de verdade, desarmada**, na janela da fábrica;
  - ela gira a cadeira para a parede de fotos, onde há uma foto dela de sete anos atrás, **sem franja**: **o mesmo ângulo, o mesmo riso**;
  - ela pensa em apagar o arquivo, não apaga e desliga a tela.
- **Tom:** silencioso, íntimo, o gancho do episódio. Claire não fala.
- **Visual:** Claire em quadros **parados**, iluminada **só pela tela do iMac**, com a parede de fotos na penumbra.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `03_LOCATIONS/APARTAMENTO_CLAIRE/apartamento_prancha.webp` | **O ateliê** (painel "Escritório / Ateliê"): mesa com iMac, estantes, câmera, **parede de fotos** |
| **R2** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | **Rosto e cor do cabelo de Claire** |
| **R3** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC007_KF-C11_V02.png` | **Claire hoje:** gola alta preta, pingente, relógio branco no pulso esquerdo |
| **R4** | `06_GENERATED_ASSETS/IMAGES/S01E02_PROP_FOTO-CLAIRE-ANTIGA_V02.png` | **A foto antiga** (Claire aos 28, sem franja, rindo): a pose a repetir no BROLL e a foto da parede |
| **R5** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC005_KF-WS-WINDOW_V02.png` | **A janela alta da fábrica** e Claire de L6 na manhã do intervalo |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC003_KF-C4_V01.png` | **A entrevista** que aparece na tela do iMac |
| **R7** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC004_KF-C7_V01.png` | **Claire de pé na fábrica, de perto** (para o BROLL) |

## 3. Personagem (traços FIXOS + look de hoje)
**CLAIRE BENNETT**, 35.
- **Rosto:** igual a R2. **Cabelo castanho-escuro, longo, ondulado, com franja cortina**; batom vinho.
- **Look de hoje à noite (em casa):**
  - **gola alta preta fina** com o **pingente vermelho-escuro por cima** e calça taupe;
  - **mangas puxadas até o antebraço**, **relógio de mostrador branco e pulseira preta no pulso ESQUERDO**, sem anéis;
  - cabelo solto, **as pontas um pouco úmidas** da chuva.
- **No BROLL (de manhã, na fábrica):** o mesmo look completo, mangas abaixadas, cabelo seco, **com franja**.

## 4. Cenário, eixos e luz
- **O ateliê de R1:**
  - a mesa com o **iMac**, de frente para uma estante;
  - a **parede de fotos** atrás de Claire, à esquerda: fotos de prédios e ruas da cidade, em P&B e em cor, molduras finas.
- **Eixo:** Claire na cadeira de escritório olha para a **DIREITA** (a tela). Para ver a parede, ela **gira a cadeira para a ESQUERDA**.
- **Luz:** **noite**. A luz principal é **a tela do iMac**, fria, no rosto dela; uma luminária baixa e quente na mesa; a parede de fotos na penumbra.
- **Texto na tela:** **só** os nomes de arquivo indicados, escritos **exatamente** como estão aqui. O resto sem texto legível.

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — Claire no ateliê (aprovar o C14 antes de tudo)
| ID | Refs | Prompt |
|---|---|---|
| **KF-C14** | R2, R3, R1 | Medium close-up, static: Claire at her desk in the dark study at night, looking toward the **RIGHT** at her iMac screen just off-frame; the cool blue-white light of the screen on her face, a low warm desk lamp behind; controlled, tired. Black turtleneck with the dark-red pendant on top, sleeves pushed up, white-dial watch with a black strap on her LEFT wrist; long dark-brown wavy hair with curtain bangs, the ends slightly damp; wine-red lipstick. Shelves in soft focus behind. 16:9, 85mm. |
| **KF-STUDY-WS** | R1, KF-C14 | The study from R1 at night: Claire sits at the desk with the iMac, seen in profile facing RIGHT toward the glowing screen, the only strong light in the room; behind her, on the LEFT, the wall of framed photographs (buildings, city streets) in half-darkness; a low desk lamp. Static wide. 16:9, 35mm. |

### Etapa 2 — Variações de Claire (Editar o C14)
| ID | Base | Prompt |
|---|---|---|
| **KF-C15** | KF-C14 | **Editar:** same image; Claire's guard drops: lips slightly parted, eyes soft and stunned, as if seeing something about herself she didn't want to see. |
| **KF-C16** | KF-C14 | **Editar:** same framing and light; she has turned her chair to the LEFT and now looks toward the LEFT side of the frame, at the photo wall off-screen; the screen light falls on the side of her face. |
| **KF-C17** | KF-C14 | **Editar:** same image, but the screen has just been switched off: her face is almost in darkness, lit only faintly by the warm desk lamp. |

### Etapa 3 — O plano de cobertura e a parede
| ID | Refs | Prompt |
|---|---|---|
| **KF-BROLL** | R4, R5, R7 | Documentary B-roll, subtle handheld, shot from a little distance: Claire at the tall arched window of the old brick factory in morning light, caught laughing FULLY and unguarded at something someone said off-screen to her right; her face in three-quarters turned to the RIGHT, **her head tilted back, eyes almost closed, the same pose and angle as R4**. Today's look: black turtleneck with the dark-red pendant, taupe trousers, watch on her LEFT wrist, long dark-brown wavy hair **with curtain bangs**. Natural window light. 16:9, 50mm. |
| **KF-WALL** | R1, R4 | The wall of framed photographs in the dark study: black-and-white and color photos of buildings, facades and city streets in thin black frames; among them, one SMALL older photo in a thin frame: the photo from R4. Half-darkness, faint light from the side. Static. 16:9, 50mm. |
| **KF-INS-PHOTO** | R4, KF-WALL | Close-up of the small framed old photo from R4 hanging on the wall at night, the worn print behind glass, faint side light. 16:9, 100mm. |

### Etapa 4 — A tela e as mãos
| ID | Base / Refs | Prompt |
|---|---|---|
| **KF-INS-FOLDER** | R1 | Close-up of an iMac screen in a dark room: a file browser window showing a list of video files with small thumbnails; the folder title reads exactly **S01_INTERVIEW_BENNETT_RAW**; other file names small and not readable. Clean modern interface, no logos. 16:9, 85mm. |
| **KF-INS-FOLDER-LAST** | KF-INS-FOLDER | **Editar:** same screen; the mouse cursor rests on the last file in the list, whose name reads exactly **B-ROLL_BREAK_03**. |
| **KF-INS-DELETE** | KF-INS-FOLDER-LAST | **Editar:** same screen; a right-click context menu is open over **B-ROLL_BREAK_03**, with the option **Delete** highlighted; the other menu items small and not readable. |
| **KF-INS-SCREEN-INT** | R6, KF-INS-FOLDER | The same iMac screen now playing a video full-screen: the image from R6 (Claire in the interview armchair), with a thin, discreet player bar at the bottom, no readable text. |
| **KF-INS-FREEZE** | KF-BROLL, KF-INS-FOLDER | The same iMac screen showing a paused video full-screen: the image from KF-BROLL (Claire laughing at the window), with a thin pause icon and player bar, no readable text. |
| **KF-INS-MOUSE** | R3, KF-C14 | Close-up in the dark: Claire's right hand on a white mouse on the desk, her index finger resting on the button, not pressing; the cool light of the screen on her skin; the black ribbed sleeve pushed up. 16:9, 100mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto (= R2) ✔/✖ · cabelo castanho-escuro com franja (nunca acobreado) ✔/✖ · figurino (gola alta, UM pingente, mangas puxadas à noite) ✔/✖ · relógio no pulso ESQUERDO ✔/✖ · sem anéis ✔/✖ · direção do olhar ✔/✖ · luz da tela no rosto ✔/✖ · texto da tela exatamente como pedido ✔/✖ · BROLL no mesmo ângulo de R4 ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **Claire:** rosto igual a R2, **franja**, gola alta com UM pingente, relógio no pulso esquerdo; olha para a **direita** (tela) e, no C16, para a **esquerda** (parede).
- **O BROLL:** o riso aberto, cabeça para trás, três-quartos para a direita, **o mesmo ângulo da foto R4**, mas **com franja** e o look de hoje.
- **A foto antiga na parede é a R4**, sem franja.
- **Os textos da tela** exatamente: `S01_INTERVIEW_BENNETT_RAW`, `B-ROLL_BREAK_03`, `Delete`.
- **A luz:** a tela como única luz forte; a parede na penumbra.
