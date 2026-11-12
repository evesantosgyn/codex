# Pacote ChatGPT — S01E01 · SC001 (refação, decupagem V03)

> **Uso:** **chat novo** no ChatGPT. Cole primeiro `00_ESTUDIO/briefing-chatgpt-keyframes.md`. Depois cole **tudo abaixo da linha**, com as imagens R1–R6 anexadas.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E01 · SC001 — "EVERYTHING UNDER CONTROL"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan. Claire Bennett, 35, arquiteta perfeccionista, vai reencontrar a ex que sumiu há sete anos.
- **Esta é a PRIMEIRA cena do episódio.** Fim de tarde de uma quinta-feira, no escritório de arquitetura de Claire. Ela e a amiga e colega Maya Reed conversam **sentadas frente a frente** na mesa de Maya, com uma **maquete arquitetônica** entre elas. Claire corrige uma árvore minúscula da maquete; Maya provoca. No fim, Claire vai embora pelo elevador. **Depois:** Claire chega em casa numa noite de chuva (SC002).
- **Visual:** a cena brinca com o **mundo em miniatura** que Claire controla: vista de cima como uma planta, câmera na altura da maquete, foco passando da árvore para Maya. Claire sempre em quadros controlados; Maya mais solta.
- **Esta cena já existe em vídeo** (R2, R4 e R6 são quadros dele). Estamos **refazendo** para corrigir continuidade. **A geografia, as roupas e as pessoas são as mesmas**; o que muda está nas regras da seção 3.

## 2. Imagens de referência para ANEXAR
| Anexo | Arquivo (repositório `evesantosgyn/codex`, pasta `SERIES_001_THE_SPACE_BETWEEN_US/`) | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/CLAIRE_BENNETT/claire-bennett_identity-pack.webp` | Rosto, corpo e acessórios de Claire |
| **R2** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | Rosto e **cor do cabelo** de Claire aprovados (é a referência que manda) |
| **R3** | `02_CHARACTERS/MAYA_REED/maya-reed_biblia-visual.webp` | Rosto, ângulos e acessórios de Maya |
| **R4** | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` | Maya aprovada, **e a geografia do lado dela**: logomarca, estante iluminada, skyline |
| **R5** | `03_LOCATIONS/ESCRITORIO_CLAIRE/escritorio_prancha-ambiente_PLANTA-A.webp` | Materiais, maquete, pasta, elevadores, luz |
| **R6** | `03_LOCATIONS/ESCRITORIO_CLAIRE/escritorio_ref-SC001_geografia-saida_t86s.jpg` | **Só a geografia** da saída (Maya à mesa, Claire indo para os elevadores pela recepção). ⚠️ **O cabelo de Claire nesse quadro está ERRADO (acobreado). Use R2 para Claire** |

## 3. Personagens (traços FIXOS)
**CLAIRE BENNETT**, 35 anos, magra e atlética, pele clara.
- **Cabelo castanho-escuro**, longo e ondulado, **com franja cortina**. **Nunca acobreado, ruivo nem claro**, nem em planos abertos.
- Olhos castanhos; sobrancelhas fortes e escuras; **batom vinho**.
- Acessórios: argolas douradas pequenas; colar duplo dourado (pingente pequeno vermelho-escuro + pingente redondo); **relógio de mostrador branco com pulseira preta no PULSO ESQUERDO**; anéis finos dourados.
- **Look:** blazer preto, blusa preta, calça preta, cinto preto.
- **Objetos dela:** **trench coat preto dobrado no encosto da cadeira**; **bolsa grande de couro preto** no chão, ao lado da cadeira; celular.

**MAYA REED**, 34 anos, pele clara **com sardas**.
- **Cabelo castanho-escuro com reflexos acobreados, cacheado, na altura do QUEIXO**; **olhos verdes**.
- Acessórios: argolas douradas; colar dourado triplo e fino; relógio de mostrador branco.
- **Look:** **blazer escuro liso (marrom-grafite)** e blusa preta.
- Expressões: divertida, provocativa, carinhosa; muitas vezes **apoia o queixo na mão**.

## 4. Cenário, eixos e luz
- **Claire Bennett Architecture Studio**, Manhattan: vidro com caixilhos pretos, madeira, grafite, piso polido, plantas.
- **Mesa de Maya:** mesa clara com uma **grande maquete branca de vários andares**, com árvores miniatura, e uma pasta preta com logo dourado (**sem texto legível**).
- **Geografia (sempre):** **Maya senta de frente para a câmera, com a recepção atrás dela**: a parede escura com a **logomarca iluminada** (pode aparecer, como em R4), a estante com luz embutida, plantas, e **os elevadores** um pouco à esquerda dela. **À direita de Maya, janelas do piso ao teto com o skyline.** **Claire senta do lado oposto, de costas para a recepção**; atrás de Claire, divisórias de vidro e o escritório.
- **Luz (igual em TODAS as imagens):** **fim de tarde, golden hour**: céu **rosa e laranja** no skyline; luz interna quente e suave; estante e logomarca iluminadas. **Atrás de Claire também é fim de tarde**: reflexos dourados e rosados no vidro, nada de fundo noturno escuro.

## 5. Keyframes (gerar nesta ordem)

### Etapa A — Plates (sem pessoas)
**KF-PLATE-M** · refs R4, R5, R6
> Cinematic still of a contemporary Manhattan architecture studio at golden hour, empty, no people. In the foreground, a light desk holding a large white multi-storey architectural model with tiny model trees. Behind the desk, the reception: a dark wall with an illuminated architectural-studio logo (no readable text beyond the logo), a backlit bookshelf, green plants, and elevator doors to the left; to the right, floor-to-ceiling windows with the Manhattan skyline under a pink and orange sunset sky. Warm interior light. 16:9, 35mm, natural film grain.

**KF-PLATE-C** · refs R5
> Cinematic still of the opposite side of the same studio desk at golden hour, empty, no people: an empty black office chair with a black trench coat folded over its back and a large black leather tote bag on the floor beside it; behind, glass partitions with black frames and the open-plan office, warm golden and pink sunset reflections on the glass, warm interior light. 16:9, 35mm, natural film grain.

### Etapa B — Inserts
| ID | Refs | Prompt |
|---|---|---|
| **KF-TOP** | R5 | Top-down overhead view, like an architectural plan, of a large white architectural model on a light desk: miniature trees, paths, the building's roof. A woman's fingers with thin gold rings enter from the edge of the frame holding the **smallest** model tree near the entrance. Warm golden-hour light, soft shadows. 16:9, photorealistic. |
| **KF-INS-TREE** | R1, R2, R5 | Macro close-up of a woman's fingers with thin gold rings and a white-dial black-strap watch on her **left wrist**, delicately adjusting the **smallest** model tree, about one centimeter tall, at the entrance of a white architectural model; shallow depth of field, warm golden-hour light. 16:9. |
| **KF-FOLDER-TOP** | R5 | Top-down view of the light desk beside the white architectural model: a black project folder with a small gold architectural logo (no readable text) sliding into frame, pushed by a hand. Warm light. 16:9. |

### Etapa C — Com as personagens
*(Claire = R1 + R2 sempre; Maya = R3 + R4 sempre. Cabelos e figurinos da seção 3.)*

| ID | Refs | Prompt |
|---|---|---|
| **KF-2S** | R1–R6 | Side two-shot at golden hour: the two women sit facing each other across the light desk, the large white architectural model between them. Claire on the **left** of the frame, leaning over the model in concentration; Maya on the **right**, chin resting on her hand, amused. Behind them, the reception logo wall, the backlit shelves, and the sunset skyline. 16:9, 35mm. |
| **KF-M1** | R3, R4, R6 | Over-the-shoulder medium shot of Maya seated at the desk facing camera, chin resting on her hand, a teasing half-smile; Claire's dark-brown hair and shoulder soft in the left foreground; behind Maya, the illuminated logo wall, backlit shelf, plants and sunset skyline on the right; model trees in the lower foreground. Warm golden-hour light. 16:9, 50mm. |
| **KF-C1** | R1, R2, R5 | Over-the-shoulder medium close-up of Claire seated, leaning over the white architectural model, focused, a perfectly straight face; Maya's curly hair soft in the right foreground; behind Claire, glass partitions catching **golden and pink sunset reflections**, warm bokeh. 16:9, 50mm. |
| **KF-MINI** | R1, R2, R5 | Low angle **from the height of the architectural model**, the camera among the tiny model trees and miniature buildings, looking **up** at Claire's face looming large above the miniature city, eyes narrowed in total concentration; warm golden light, shallow depth of field on the foreground trees. Comic sense of scale. 16:9, 24mm. |
| **KF-RACK** | R3, R4, R5 | Macro shot from Claire's side: in sharp focus in the foreground, the smallest model tree at the model's entrance; in the soft background, **Maya out of focus**, seated, chin on hand, watching; the logo wall and sunset behind her. 16:9, 85mm, very shallow depth of field. |
| **KF-C2** | R1, R2, R5 | Medium shot of Claire seated, holding the black project folder open, reading, dry and half-attentive; golden sunset reflections on the glass behind her. 16:9, 50mm. |
| **KF-C3** | R1, R2 | Close-up of Claire looking up for the first time, a guarded flicker of attention; warm golden light, sunset bokeh behind. 16:9, 85mm. |
| **KF-EYES** | R1, R2 | Extreme close-up of **only Claire's eyes and curtain bangs** looking up over the top edge of the black folder, unamused, deadpan. Warm light. 16:9, 100mm. |
| **KF-DEEP** | R1–R6 | Deep-focus composition like R6: **Maya in the right foreground**, seated at the desk with the model, turned to look over her shoulder; **Claire in the background**, walking away from camera across the reception toward the elevators, the **black trench coat over her arm** and the large black bag on her shoulder, phone in hand. **Claire's hair is dark brown, long and wavy (NOT copper).** Logo wall and sunset skyline. 16:9, 35mm. |
| **KF-TELE** | R1, R2, R5, R6 | Long telephoto shot from across the studio toward the elevators: Claire stands inside an open elevator, facing out, trench coat over her arm, bag on her shoulder, deadpan with a micro-smile; the elevator doors open; foreground slightly soft. **Dark-brown hair.** Warm light. 16:9, 135mm. |
| **KF-M2** | R3, R4 | Close-up of Maya at the desk, turned looking over her shoulder toward the elevators, a fond, amused smile, shaking her head slightly; sunset light on her face. 16:9, 85mm. |

## 6. Critérios de aprovação
- Claire: **cabelo castanho-escuro em todas** (atenção máxima em KF-DEEP e KF-TELE), franja, batom vinho, **relógio no pulso esquerdo**.
- Maya: cabelo **na altura do queixo**, olhos verdes, sardas, blazer escuro liso.
- Geografia: Maya de frente, com a logomarca, as estantes e os elevadores atrás; Claire do lado oposto.
- **O mesmo pôr do sol** em todas as imagens, inclusive atrás de Claire.
- Trench dobrado na cadeira (PLATE-C) e **no braço de Claire** na saída (DEEP, TELE).
- Nenhum texto legível além da logomarca; nenhuma pessoa extra em primeiro plano.
