# Pacote ChatGPT — S01E01 · SC006

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha**, com as imagens R1–R6 anexadas.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E01 · SC006 — "PROFESSIONAL BOUNDARIES"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Antes:** Claire Bennett, 35, arquiteta, foi surpreendida na noite anterior pela ex, Olivia, que sumiu há sete anos. Hoje de manhã contou à amiga Maya.
- **Esta cena:** **sexta-feira de manhã**, na **sala de reuniões de vidro** do escritório de Claire. Claire apresenta o projeto de restauração de um prédio antigo para Maya e dois membros da equipe de requalificação. Um slide revela que a documentarista do projeto é Olivia. Claire perde o fio, tenta disfarçar e só piora.
- **Visual:** Claire em quadros parados e simétricos (o controle dela); Maya com leve câmera na mão.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/CLAIRE_BENNETT/claire-bennett_identity-pack.webp` | Rosto, corpo e looks de Claire (usar o look da **camisa de seda preta + calça creme**) |
| **R2** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | Rosto e **cor do cabelo** de Claire aprovados (é a referência que manda) |
| **R3** | `02_CHARACTERS/MAYA_REED/maya-reed_biblia-visual.webp` | Rosto, ângulos e looks de Maya (usar o **"Minimalista e elegante": camisa e calça pretas**) |
| **R4** | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` | Rosto e cabelo de Maya aprovados |
| **R5** | `03_LOCATIONS/ESCRITORIO_CLAIRE/escritorio_prancha-ambiente_PLANTA-A.webp` | O escritório; **o render "Sala de reuniões"** é a base desta sala |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E01_SC001_KF-PLATE-M_V01.png` | Materiais do escritório (vidro com caixilho preto, madeira, maquete branca) |

⚠️ R2, R4 e R6 são de **fim de tarde (pôr do sol)**. Use-os só para rostos e materiais. **A luz desta cena é de DIA NUBLADO.**

## 3. Personagens (traços FIXOS + look da cena)
**CLAIRE BENNETT**, 35.
- Rosto igual a R2; **cabelo castanho-escuro, longo, ondulado, com franja** (nunca acobreado); sobrancelhas fortes; **batom vinho**.
- **Look:** **camisa de seda preta** + **calça pantalona creme**, cinto preto; argolas douradas; colar duplo dourado (pingente vermelho-escuro + pingente redondo); **relógio de mostrador branco e pulseira preta no PULSO ESQUERDO**; anéis finos.
- De pé, segura um **controle remoto** de apresentação. Postura impecável.

**MAYA REED**, 34.
- Rosto igual a R4; **cabelo castanho-escuro com reflexos acobreados, cacheado, na altura do QUEIXO**; **olhos verdes**; sardas.
- **Look:** **camisa e calça pretas**; argolas; colar triplo fino; relógio de mostrador branco.
- Sentada, com um **laptop** à frente.

**EQUIPE DE REQUALIFICAÇÃO** (figurantes, sem falas, sempre secundários):
- **Homem de uns 50 anos, terno cinza**, gravata discreta.
- **Mulher de uns 40, cardigã e óculos**, bloco de notas.

## 4. Cenário, eixos e luz
- **Sala de reuniões com paredes de vidro e caixilhos pretos** (base: o render "Sala de reuniões" de R5): **mesa longa de madeira**, cadeiras pretas; **uma grande maquete arquitetônica branca no centro da mesa**; **tela de apresentação grande na parede de fundo**; janelas do piso ao teto com o skyline.
- **Posições:** **Claire de pé, à DIREITA da tela**, de frente para a mesa. **Maya sentada** na ponta da mesa mais próxima da câmera, do lado esquerdo. Os dois figurantes sentados ao longo da mesa.
- **Luz:** **dia nublado**, luz difusa e fria pelas janelas, skyline acinzentado; luz interna neutra e quente. Nada de pôr do sol.
- **A tela:** sempre **branca, lisa, sem nada escrito** (os slides entram na pós).
- Sem texto legível em lugar nenhum.

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — Cenário
**KF-PLATE-ROOM** · R5, R6
> The glass-walled conference room of a contemporary Manhattan architecture studio on an overcast day, no people: black-framed glass walls, a long wooden table with black chairs, a large white architectural model at the center of the table, a large blank white presentation screen on the far wall, floor-to-ceiling windows with a grey, overcast Manhattan skyline. Soft diffuse daylight, warm neutral interior light. 16:9, 28mm, photorealistic.

### Etapa 2 — Claire (aprovar o KF-C1 antes de seguir)
| ID | Refs | Prompt |
|---|---|---|
| **KF-C1** | R1, R2, PLATE-ROOM | Medium shot: the woman from R2 stands to the right of the blank white presentation screen in the glass conference room, facing the table, holding a slim presentation remote, composed and in control. Black silk blouse, cream wide-leg trousers, black belt, wine-red lipstick, gold hoops, double gold necklace, white-dial watch with black strap on her LEFT wrist. Dark brown long wavy hair with curtain bangs. Overcast daylight from the windows. Symmetrical, static framing. 16:9, 50mm. |
| **KF-C2** | R1, R2 | Close-up of Claire (same side as KF-C1), the composure cracking almost imperceptibly: a held breath, eyes fixed on the screen off to the side. Wine-red lipstick, dark brown hair with bangs, gold hoops. Soft overcast light. 16:9, 85mm. |
| **KF-OTS-SCREEN** | R1, R2, PLATE-ROOM | Over-the-shoulder from behind Claire (her dark brown hair and black silk blouse soft in the right foreground) looking at the large presentation screen, which is plain bright white with nothing on it. 16:9, 35mm. |
| **KF-INS-REMOTE** | R1 | Close-up of Claire's hand with thin gold rings and a white-dial black-strap watch on her LEFT wrist pressing a button on a slim black presentation remote; black silk cuff. 16:9, 85mm. |

### Etapa 3 — Maya, equipe e plano geral
| ID | Refs | Prompt |
|---|---|---|
| **KF-M1** | R3, R4, PLATE-ROOM | Medium shot of the woman from R4 seated at the near end of the long table, a laptop in front of her, looking up toward the presentation; black shirt, curly chin-length dark brown hair with copper highlights, green eyes, freckles, gold hoops. The white model on the table, glass walls behind. Overcast daylight. 16:9, 50mm. |
| **KF-M2** | R3, R4 | Close-up of Maya, eyes narrowed in suspicion, glancing from the screen toward Claire off-frame; a knowing half-smile beginning. Overcast light. 16:9, 85mm. |
| **KF-TEAM** | PLATE-ROOM | Medium shot of two people seated along the conference table: a man in his fifties in a grey suit and a woman in her forties in a cardigan and glasses with a notepad, exchanging a puzzled glance. Overcast light, glass walls. 16:9, 50mm. |
| **KF-INS-SCREEN** | PLATE-ROOM | Front view of the large presentation screen on the wall of the conference room, plain bright white, nothing on it; edges of the room visible. 16:9, 35mm. |
| **KF-WS** | R1–R6, PLATE-ROOM | Wide shot of the glass conference room: Claire standing to the right of the blank white screen with the remote; Maya seated at the near end of the table with a laptop; the man in the grey suit and the woman in the cardigan seated along the table; the white model at the center. Overcast daylight. 16:9, 24mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto ✔/✖ · cabelo ✔/✖ · figurino ✔/✖ · relógio (pulso esquerdo) ✔/✖ · cenário ✔/✖ · luz (dia nublado) ✔/✖ · tela branca / sem texto ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção antes de seguir.

## 7. Critérios de aprovação
- **Claire:** rosto igual a R2; cabelo castanho-escuro com franja; **batom vinho**; seda preta + creme; relógio no pulso esquerdo.
- **Maya:** rosto igual a R4; cachos no queixo; olhos verdes; preto.
- Sala de vidro com a maquete no centro e a tela no fundo; **dia nublado**.
- **Tela sempre branca**; nenhum texto legível.
