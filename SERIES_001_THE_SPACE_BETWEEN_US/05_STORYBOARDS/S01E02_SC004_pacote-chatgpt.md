# Pacote ChatGPT — S01E02 · SC004 "Did You Know?"

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha**, com as imagens R1–R9 anexadas.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E02 "FAMILIAR STRANGERS" · SC004 "DID YOU KNOW?"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Terça de manhã, no set de entrevista da fábrica, logo depois da entrevista.** A câmera para de gravar, e a equipe sai para o intervalo. Claire Bennett e Olivia Hayes ficam sozinhas.
- **A cena:** Claire tira o microfone e devolve a Olivia. Pergunta se Olivia sabia que o projeto era dela quando bateu à porta. Olivia diz que sim. Claire se levanta e diz: "You don't get to decide that for me. Not again." Depois vai embora pelo salão.
- **Tom:** sério, contido, sem gritos. É a cena mais dramática do episódio.
- **Visual:** Claire em quadros **parados**; Olivia com leve câmera na mão.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` | **Rosto e cor do cabelo de Claire** |
| **R2** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC003_KF-C3_V01.png` | **Claire nesta manhã:** na poltrona, gola alta, pingente, microfone na gola |
| **R3** | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` | **Rosto de Olivia** (pinta) |
| **R4** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-O3_V01.png` | **Olivia nesta manhã:** suéter marrom, coque, pinta visível, tatuagem |
| **R5** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-SET-WS_V02.png` | **O set:** poltrona, caixote, painel de LED, câmera, janelas |
| **R6** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-C1-B_V01.png` | **A poltrona e o caixote com o copo d'água** |
| **R7** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC003_KF-INS-REC_V01.png` | **A câmera e a luz de gravação** |
| **R8** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC002_KF-INS-MIC_V01.png` | **O microfone de lapela e o cabo** |
| **R9** | `03_LOCATIONS/FABRICA_RESTAURACAO/fabrica_ref-salao.png` | **O salão:** colunas de ferro, piso de madeira, janelas altas em arco |

## 3. Personagens (traços FIXOS + look de hoje)
**CLAIRE BENNETT**, 35.
- Rosto igual a R1; **cabelo castanho-escuro, longo, ondulado, com franja cortina**; batom vinho.
- **Look:** **gola alta preta fina** com o **pingente vermelho-escuro por cima**, **calça taupe**, cinto preto, botas pretas; argolas douradas; **relógio de mostrador branco e pulseira preta no PULSO ESQUERDO**; unhas naturais. Sem capacete.
- **Microfone:** na gola **só no KF-C5** (quando ela o solta). **Depois disso, sem microfone.**

**OLIVIA HAYES**, 33.
- Rosto igual a R3; **UMA pinta pequena logo abaixo do lábio inferior, do LADO ESQUERDO dela**.
- **Look:** suéter de tricô marrom de ombro caído, **jeans**, coque bagunçado loiro-escuro, argolas pequenas, colares finos; **tatuagem pequena de câmera no antebraço interno ESQUERDO**; **SEM relógio**; **sem fone** nesta cena.

## 4. Cenário, eixos e luz
- **O set de R5:** poltrona de couro caramelo com estrutura de metal preto; caixote de madeira clara com o copo d'água (R6); o painel de LED num tripé, agora **DESLIGADO**; a câmera no tripé; as janelas altas em arco; o salão com colunas de ferro (R9).
- **Posições:**
  - **Claire sentada na poltrona** até o KF-C6; **de pé**, ao lado da poltrona, no 2S-STAND e no C7.
  - **Olivia de pé**, à direita de Claire, ao lado da poltrona.
- **Eixo:** **Claire olha para a DIREITA** (para cima quando sentada, reto quando de pé). **Olivia olha para a ESQUERDA** (para baixo enquanto Claire está sentada, reto depois).
- **Luz:** **o painel de LED está apagado.** Só a luz natural de manhã pelas janelas altas, mais crua e lateral. **Nenhuma luz de set no rosto de Claire.**
- **Sem texto legível.**

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — O fim da gravação
| ID | Refs | Prompt |
|---|---|---|
| **KF-INS-REC-OFF** | R7 | Same as R7: close-up of the cinema camera body on its tripod in the factory set, but the small recording tally light is now **OFF** (dark, no red glow). Same framing and light. 16:9, 100mm. |
| **KF-SET-BREAK** | R5, R2 | The interview set from R5 a moment after recording stops: the LED light panel on its stand is now **switched off** (dark); the crew walking away out of focus in the background; Claire still seated in the caramel armchair, microphone on her collar, looking down. Natural morning window light only. 16:9, 28mm. |

### Etapa 2 — Claire sentada e Olivia de pé (aprovar o KF-C6 antes de seguir)
| ID | Refs | Prompt |
|---|---|---|
| **KF-C5** | R1, R2, R8 | Medium shot, static: Claire seated in the caramel armchair, unclipping the small black lavalier microphone from her turtleneck herself, eyes down, composed. LED off: only natural window light. Watch on her LEFT wrist. 16:9, 50mm. |
| **KF-O4** | R3, R4, R5 | Medium shot: Olivia standing beside the armchair, hands empty at her sides, looking **down and toward the LEFT** at Claire seated off-screen; not moving to help. No headphones, no wristwatch. Natural window light, the switched-off LED panel behind her. 16:9, 50mm. |
| **KF-C6** | R1, R2 | Close-up of Claire seated, **no microphone now**, looking **up and toward the RIGHT** at Olivia standing; steady, controlled, asking a question that matters. Only the natural window light on her face, rawer than before. 16:9, 85mm. |
| **KF-O5** | R3, R4 | Close-up of Olivia standing, looking **down and toward the LEFT**, the microphone cable wound around her fingers at chest height; honest, exposed, not defending herself. ONE beauty mark clearly visible below her lower lip on her LEFT side. Natural window light. 16:9, 85mm. |

### Etapa 3 — Inserts
| ID | Refs | Prompt |
|---|---|---|
| **KF-INS-HANDOFF** | R2, R8 | Close-up: Claire's hand (white-dial watch on her LEFT wrist, natural nails) holding out the small black lavalier microphone with its cable; Olivia's hand (thin gold rings, camera tattoo on the inner left forearm, brown knit sleeve) taking it. Natural window light. 16:9, 100mm. |
| **KF-INS-CABLE** | R8, R4 | Close-up: Olivia's fingers slowly winding the thin black microphone cable around her fingers; brown knit sleeve; camera tattoo visible. 16:9, 100mm. |

### Etapa 4 — De pé e a saída
| ID | Refs | Prompt |
|---|---|---|
| **KF-2S-STAND** | KF-C6, KF-O5, R5 | Two-shot in profile: Claire, now **standing** beside the armchair on the LEFT, straightening her turtleneck; Olivia standing on the RIGHT, the cable in her fingers; the two at **the same eye level**, about half a meter apart. Static. Natural window light, the switched-off LED behind them. 16:9, 35mm. |
| **KF-C7** | R1, R2, KF-2S-STAND | Close-up of Claire **standing**, looking **straight toward the RIGHT** at eye level; her voice level but it costs her something; firm, hurt, dignified. No microphone. 16:9, 85mm. |
| **KF-O6** | R3, R4, KF-2S-STAND | Close-up of Olivia standing, looking **straight toward the LEFT** at eye level, hit by what she just heard; the cable still wound around her fingers. ONE beauty mark below her lower lip on her LEFT side. 16:9, 85mm. |
| **KF-WS-EXIT** | R9, KF-2S-STAND | Wide static shot of the factory floor (R9): in the soft-focus foreground, Olivia **from behind**, standing still, messy bun, brown sweater; in the background, Claire, small in the frame, walking away between the iron columns toward the tall bright arched windows. Morning light in shafts with dust. 16:9, 35mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto ✔/✖ · cabelo (Claire castanho-escuro) ✔/✖ · pinta (Olivia, UMA) ✔/✖ · figurino (Claire calça taupe; Olivia jeans, sem relógio, sem fone) ✔/✖ · microfone (só no C5) ✔/✖ · LED apagado ✔/✖ · direção do olhar ✔/✖ · relógio no pulso esquerdo (Claire) ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **Claire:** rosto igual a R1; franja; batom vinho; gola alta com o pingente; calça taupe; relógio no pulso esquerdo; **microfone só no C5**; sentada até o C6, de pé no 2S-STAND e no C7; olha para a **direita**.
- **Olivia:** rosto igual a R3; **uma pinta**; suéter marrom, jeans; tatuagem; **sem relógio, sem fone**; olha para a **esquerda**; o cabo nos dedos no O5 e no O6.
- **Luz:** **LED apagado**, só a luz das janelas.
- **O mesmo set** de R5 e R6: poltrona de metal preto, caixote com o copo.
