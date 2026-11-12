# S01E01 · SC002 — A PERFECTLY ORDINARY NIGHT · Decupagem V01

**Status:** ✅ **APROVADA** (2026-11-12): todos os itens, inclusive a câmera na geladeira (SH07), o trench preto e a P16 · **Roteiro:** Screenplay V3.2 (APROVADO) · **Data:** 2026-11-12
**Duração do roteiro:** 1:25 · **Soma dos planos (montagem):** 1:26 · **23 planos, 2 eixos**
**Ferramenta:** MiniMax H3 (gerações de 5 s no mínimo, cortadas na montagem) · LoRA de Claire · voz `claire_bennett_voice-ref_v02.wav`

## Resumo da cena

| Campo | Definição |
|---|---|
| Locação | Apartamento de Claire (planta corrigida em texto): **Entrada (1)**, a sudoeste → faixa oeste → **Cozinha (4)**, a noroeste, com a ilha de mármore de frente para as janelas norte |
| Período | **Quinta-feira, noite, chuva** (cronologia aprovada) |
| Intenção dramática | Estabelecer a tranquilidade que será interrompida. A rotina é elegante, mas excessiva: o perfeccionismo de Claire **não funciona tão bem fora do escritório**. Terminar com a expectativa de uma entrega banal, para que a batida na porta engane o público junto com ela. |
| Estratégia visual | Continua a regra de Claire (**câmera estática, composição limpa**), mas agora com **espaço demais à volta dela**: lentes mais abertas, Claire pequena em quadros grandes e bonitos. A solidão aparece sem ser dita. O humor fica nos **inserts** (a chave torta, a geladeira "cheia de ambição"). A geladeira tem o único ponto de vista "brincalhão" da cena (câmera de dentro dela). **Sem nenhum movimento de câmera**: a tranquilidade é estática, até a batida. |
| Ritmo | Começo lento e silencioso (chegada) → ping-pong rápido na ligação → suspensão (notificação, "Finally") → **batida** → caminhada até a porta. |
| Geografia e eixos | **Eixo N (cozinha):** câmera olhando para o norte, para a ilha, com as **janelas de chuva e a cidade** ao fundo. **Eixo S (entrada):** câmera olhando para o sul, para a porta, com fundo interior quente. Claire anda **sempre pela faixa oeste**: entrada → cozinha (de costas para a câmera do eixo S) e cozinha → porta (de costas para a câmera do eixo N). |
| Luz (regra L2) | Noite. **Âmbar quente** dos práticos (luminária do aparador, pendentes âmbar da ilha, luminária arco) contra o **azul frio** da cidade e de uma luz perto da janela ("a cooler blue glow", roteiro). Chuva escorrendo no vidro, reflexos. **Os dois eixos com o mesmo estado:** mesma intensidade de chuva, mesmas luzes acesas, mesmo céu noturno. Na geladeira, a luz branca fria dela faz o rosto de Claire, como um alívio cômico de cor. |
| Looks (regra L3) | **Claire:** chega com **casaco trench preto (L3) com os ombros molhados**, vestido fora de quadro entre o elevador e a rua, por cima do L1 (blazer e blusa pretos da SC001, **mesmos acessórios**: argolas, colar duplo, relógio de pulseira preta, anéis), **bolsa preta grande de couro** no ombro e celular. Pendura o casaco **e o blazer** e fica de blusa preta de manga longa (decisão V17). |
| Objetos | Prato de cerâmica das chaves e chaves · cabideiro ou gancho junto à porta · bolsa preta · celular (telas compostas na pós) · geladeira (água com gás, legumes arrumados, queijo caro, pote de massa com etiqueta de data) · copo d'água · ilha de mármore |
| Personagens | Claire (em quadro); **Maya só em V.O. (viva-voz)** |
| Pendências | **P12:** geografia da entrada e look de Claire em casa precisam bater com os keyframes travados da SC003 → **SH01–SH04, SH22–SH23 dependem de P12**. **P16 (nova):** método para gerar falas fora de quadro (V.O. de Maya) → **o áudio de SH13–SH18 depende de P16**. |

## Checklist pré-geração (resumo)

| Bloco | Situação na SC002 |
|---|---|
| 1. Herança | Claire: **vídeo aprovado da SC001** (rosto, franja, castanho-escuro, batom, colar, relógio, bolsa). Apartamento: sem vídeo aprovado; **os keyframes da SC003 prevalecem** quando chegarem (P12) |
| 2. Transição | SC001 saída: blazer preto + bolsa + celular, sem casaco → SC002 entrada: **+ trench preto molhado**. Casaco pendurado (SH03); bolsa no aparador (SH02). Blazer: tirar ou manter conforme a SC003 |
| 3. Identidade | Planos de risco L1 (abertos e de caminhada): **SH01, SH06, SH23**. Usar LoRA + Identity Pack frontal e 3/4 + quadro do plano anterior + "dark brown hair" no texto |
| 4. Luz | Plate do eixo N e plate do eixo S gerados juntos, com o mesmo estado de chuva e de luzes; conferidos lado a lado antes das gerações com Claire |
| 5. Objetos e escala | A chave "slightly crooked" tem que estar visivelmente torta no insert. Objetos novos (prato de cerâmica, cabideiro) entram em `continuidade.yaml` quando forem aprovados |
| 6. Voz | Claire: `claire_bennett_voice-ref_v02.wav` em todos os planos em que fala. Maya (V.O.): P16 |
| 7. Técnico | Gerar 5 s (mínimo do H3) e cortar na montagem. Master 3840 × 2160 |

## Lista de planos

| Shot ID | Montagem | Eixo / tamanho | Ação | Intenção | Áudio | Depende de |
|---|---|---|---|---|---|---|
| S01E01_SC002_SH01 | 4 s | S · WS (porta ao fundo) | A porta se abre; Claire entra, molhada, bolsa no ombro, e fecha a porta | Chegada ao "território controlado" | Chuva abafada; porta; passos | P12 |
| S01E01_SC002_SH02 | 3 s | S · insert | A mão de Claire deposita as chaves no prato de cerâmica do aparador (a bolsa já está sobre o aparador) | Rotina | Chaves na cerâmica | P12 |
| S01E01_SC002_SH03 | 4 s | S · MS | Claire pendura o trench no cabideiro junto à porta | Rotina elegante | Tecido; chuva | P12 |
| S01E01_SC002_SH04 | 3 s | S · ECU insert | Uma chave **ligeiramente torta** no prato; o dedo de Claire a endireita | **Humor:** o excesso | Tilintar mínimo | — |
| S01E01_SC002_SH05 | 3 s | S · insert | Celular na mão; **tela composta:** *"Your order is on its way."* | Plantar a entrega | **BUZZ** | — |
| S01E01_SC002_SH06 | 4 s | N · WS | Claire atravessa a faixa oeste rumo à cozinha; janelas de chuva ao fundo | Espaço grande, mulher sozinha | Passos; chuva mais presente perto das janelas | — |
| S01E01_SC002_SH07 | 4 s | N · MS, **câmera dentro da geladeira** | Claire abre a geladeira; a luz fria dela acende o rosto | Expectativa cômica | Porta da geladeira; zumbido | — |
| S01E01_SC002_SH08 | 3 s | insert (POV de Claire) | Conteúdo: água com gás, legumes arrumadíssimos, queijo caro, quase nada que pareça jantar | **Humor:** a geladeira de uma perfeccionista | Zumbido | — |
| S01E01_SC002_SH09 | 4 s | N · MCU (luz da geladeira) | Claire avalia o conteúdo, impassível | Autoironia | **CLAIRE** (to herself): "Excellent. A refrigerator full of ambition." | — |
| S01E01_SC002_SH10 | 4 s | insert | Mão tira o pote de massa e gira para ler a etiqueta de data (**ilegível**: o gesto conta) | Esperança breve | Plástico | — |
| S01E01_SC002_SH11 | 4 s | N · MS | Claire devolve o pote e fecha a geladeira; o celular **toca** | Derrota pequena; corte pela ligação | Porta; **toque do celular** | — |
| S01E01_SC002_SH12 | 2 s | insert | **Tela composta:** chamada de *MAYA* | Quem liga | Toque | — |
| S01E01_SC002_SH13 | 4 s | N · MS na ilha | Claire atende no viva-voz e pousa o celular no mármore | Seca, sem cerimônia | **CLAIRE:** "What?" | P16 (áudio de Maya a seguir) |
| S01E01_SC002_SH14 | 4 s | N · MCU | Claire ouve e responde | Defensiva | **MAYA (V.O.):** "That's a lovely way to greet someone." / **CLAIRE:** "I assumed it was an emergency." | P16 |
| S01E01_SC002_SH15 | 4 s | N · MCU | Claire ouve (gerado **sem fala**); olha de relance para a geladeira, culpada | Pega no flagra | **MAYA (V.O.):** "It is. I'm checking whether you've eaten something that wasn't prepared by a restaurant." | P16 |
| S01E01_SC002_SH16 | 7 s | N · MCU | Claire responde em evasivas, cada vez mais curtas | **Ping-pong**: a mentira desmorona | **CLAIRE:** "I had a salad." / **MAYA (V.O.):** "When?" / **CLAIRE:** "Recently." / **MAYA (V.O.):** "Claire." / **CLAIRE:** "Monday." | P16 |
| S01E01_SC002_SH17 | 4 s | N · CU | Claire, digna e absurda | Golpe final | **MAYA (V.O.):** "It's Thursday." / **CLAIRE:** "Time is a social construct." / Maya ri (V.O.) | P16 |
| S01E01_SC002_SH18 | 4 s | N · MS | Um quase-sorriso; Claire encerra a ligação com um toque | Carinho escondido | **MAYA (V.O.):** "Good night, you terrifying woman." / **CLAIRE:** "Good night." | P16 |
| S01E01_SC002_SH19 | 3 s | insert | Celular sobre o mármore; **tela composta:** *"Your courier is nearby."* | A espera | Notificação | — |
| S01E01_SC002_SH20 | 4 s | N · MCU | Claire expira, aliviada, e estende a mão para um copo d'água | Alívio banal: **a armadilha** | **CLAIRE:** "Finally." | — |
| S01E01_SC002_SH21 | 3 s | N · MCU | **KNOCK.** Claire congela com o copo na mão e olha para a entrada (olhar para a esquerda do quadro) | A rotina se quebra | **Batida suave** na porta | — |
| S01E01_SC002_SH22 | 2 s | insert | O celular sobre o mármore acende de novo (**tela composta:** notificação de entrega) | Reforça o engano: "é o entregador" | Notificação | P12 (não deve revelar quem está na porta) |
| S01E01_SC002_SH23 | 4 s | N · WS invertido (câmera na cozinha olhando para o sul) | Claire caminha pela faixa oeste até a porta, de costas, menor a cada passo | Ela vai abrir para o desconhecido | Passos; chuva | P12 |

**Total na montagem: ~86 s (1:26).** Gerações: 23 × 5 s.

> **CUT TO:** SC003 (travada). O enquadramento final da SH23 (porta ao fundo, Claire chegando) precisa casar com o primeiro keyframe travado da SC003.

## Keyframes (image-to-video)
Ordem recomendada:
1. **Plate do eixo N** (cozinha + janelas com chuva, noite) e **plate do eixo S** (entrada, porta, aparador com prato, cabideiro), juntos, com a mesma luz (L2). **Conferir o plate S com os keyframes da SC003 antes de aprovar (P12).**
2. **Claire em casa:** um keyframe-mestre por eixo, a partir da LoRA + Identity Pack + um quadro do vídeo da SC001 (para casar rosto, cabelo e acessórios).
3. **Inserts** (chaves, geladeira, pote, celular com tela verde ou neutra para composição).
4. **Último quadro** da SH23 = composição do primeiro keyframe da SC003 (corte invisível).

## Prompts para o MiniMax H3

**Entradas comuns de cada geração com Claire:**
- **Primeiro quadro:** keyframe aprovado do plano.
- **Referências de imagem:** `claire-bennett_identity-pack.webp` (frontal + 3/4) · plate do eixo · último quadro do plano anterior · 1 quadro da SC001 (rosto e cabelo).
- **Referência de áudio** (só em planos em que Claire fala): `claire_bennett_voice-ref_v02.wav`.
- **Duração:** 5 s. Proporção 16:9.

**Frase fixa de identidade** (só em planos abertos e de caminhada, regra L1): *"Her hair stays dark brown, long and wavy with curtain bangs."*

| Shot | Prompt (EN) |
|---|---|
| SH01 | Wide shot from inside a dim, elegant Manhattan apartment entrance at night, facing the dark wooden front door. The door opens and Claire steps in from the hallway, her black trench coat damp at the shoulders, a large black leather bag on her shoulder; she closes the door behind her. Static camera. Warm amber light from a console lamp and wall sconce, round mirror, vase of red branches; muffled rain. Her hair stays dark brown, long and wavy with curtain bangs. No dialogue; soft rain and the door closing. |
| SH02 | Close insert of a dark wood console table at night. A woman's hand with thin gold rings and a black-strap watch drops a set of keys into a small ceramic dish; a large black leather bag rests beside it. Static camera, warm lamp light. Sound of keys on ceramic. |
| SH03 | Medium shot at the apartment entrance at night. Claire takes off her damp black trench coat and hangs it on a coat hook beside the door. Static camera. Warm amber lamp light; calm, practiced movement. No dialogue; fabric rustle, rain. |
| SH04 | Extreme close-up of keys lying in a small ceramic dish; one key sits slightly crooked. A single finger enters frame and nudges it until it is perfectly aligned with the others, then withdraws. Static camera, warm light, shallow depth of field. A tiny metallic click. |
| SH05 | Close insert of a woman's hand holding a smartphone, screen facing camera and showing a plain bright neutral screen (to be replaced in post). The phone vibrates once. Static camera, warm light. A short phone buzz. |
| SH06 | Wide shot inside a large, quiet, elegant apartment at night. Claire, in a black blazer and black top, walks away from camera along the west wall toward the kitchen island; floor-to-ceiling windows ahead streaked with rain, the Manhattan skyline glowing blue beyond. Static camera. Warm amber pendants over a marble island, cool blue light near the window. Her hair stays dark brown, long and wavy with curtain bangs. Footsteps, rain on glass. |
| SH07 | Medium shot from inside a refrigerator looking out, framed by shelves with sparkling water bottles. The door opens and Claire looks in; the cold white fridge light falls on her face, the warm kitchen glowing behind her. Static camera. Neutral, evaluating expression. Fridge door sound and hum. |
| SH08 | Insert, Claire's point of view into an open refrigerator: neatly arranged sparkling water, perfectly aligned vegetables, an expensive wedge of cheese, one plastic container of leftover pasta, almost nothing resembling dinner. Static camera, cold fridge light. Fridge hum. |
| SH09 | Medium close-up of Claire lit by cold white refrigerator light, the warm kitchen behind her. She studies the contents with a perfectly straight face, a dry, self-mocking flicker in her eyes. Static camera. Claire says quietly to herself: "Excellent. A refrigerator full of ambition." Fridge hum. |
| SH10 | Close insert in cold fridge light: a woman's hand takes out a plastic container of pasta and turns it to read a small date label (label not legible), pauses. Static camera. Plastic sounds. |
| SH11 | Medium shot in the kitchen at night. Claire puts the container back and closes the refrigerator; the room returns to warm amber light, rain on the windows behind her. Just as the door shuts, she glances toward her phone. Static camera. Fridge door closes; a phone starts ringing. |
| SH12 | Close insert of a smartphone lying on a white marble counter, plain bright neutral screen (incoming call to be composited in post), vibrating. Static camera, warm pendant light. Ringtone. |
| SH13 | Medium shot of Claire at the marble kitchen island at night, rain-streaked windows and city lights behind her. She taps her phone to answer on speaker and sets it down on the counter. Static camera. Warm amber pendants, cool blue window light. Claire says flatly: "What?" Rain ambience. |
| SH14 | Medium close-up of Claire at the kitchen island, looking down at the phone on the counter. She listens for a beat, then answers, slightly defensive. Static camera. Warm amber light on her face, blue city bokeh behind. Claire says: "I assumed it was an emergency." Rain ambience. |
| SH15 | Medium close-up of Claire at the kitchen island listening to a call on speaker. She says nothing; her eyes slide guiltily toward the refrigerator, then back. Static camera, warm amber light, blue city bokeh. No dialogue; rain ambience only. |
| SH16 | Medium close-up of Claire at the kitchen island answering a friend on speakerphone with increasingly short, evasive replies, pausing to listen between them. Static camera, warm amber light, rain-streaked windows behind. Claire says: "I had a salad." … "Recently." … "Monday." Rain ambience. |
| SH17 | Close-up of Claire, chin slightly raised, perfectly dignified and absurd. Static camera, warm amber light. Claire says, deadpan: "Time is a social construct." Rain ambience. |
| SH18 | Medium shot of Claire at the kitchen island. An almost-smile tugs at her mouth as she listens; she says "Good night." and ends the call with one tap on the phone. Static camera, warm amber light, rain behind. Rain ambience. |
| SH19 | Close insert of the smartphone on the marble counter, plain bright neutral screen (delivery notification to be composited in post), lighting up once. Static camera, warm light. Notification chime. |
| SH20 | Medium close-up of Claire at the kitchen island. She exhales, relieved, and reaches for a glass of water. Static camera, warm amber light, rain-streaked windows behind. Claire says softly: "Finally." Rain ambience. |
| SH21 | Medium close-up of Claire holding a glass of water at the kitchen island. A quiet knock sounds; she freezes mid-motion and turns her eyes toward the apartment entrance, screen-left. Static camera, warm amber light. A soft knock at the door, rain. |
| SH22 | Close insert of the smartphone on the marble counter lighting up again, plain bright neutral screen (delivery notification composited in post). Static camera, warm light. Notification chime. |
| SH23 | Wide shot from the kitchen looking south toward the front door at the far end of the apartment. Claire sets down her glass and walks away from camera along the west wall toward the door, smaller with each step. Static camera. Warm amber lamps by the entrance, rain reflections on the floor from the windows. Her hair stays dark brown, long and wavy with curtain bangs. Footsteps, rain. |

**Frases que valem como "negativos" (o H3 não tem campo próprio ❓):** acrescentar em todos os planos com Claire: *"Her face, eye color and hair remain consistent; natural hand anatomy; no on-screen text; no extra people."*

## Áudio e direção de interpretação

**Camadas:** (1) diálogo de Claire (gerado no H3 com a referência v02) · (2) **Maya V.O.** (P16) com EQ de alto-falante de celular · (3) ambiência: **chuva constante** (mais forte no eixo N, junto às janelas), cidade distante, zumbido da geladeira · (4) SFX: porta, chaves, tecido, buzz, toque, notificações, **batida** · (5) música: **nenhuma**, para que a batida caia no silêncio.

| Fala | Intenção | Pausa / respiração | Intensidade |
|---|---|---|---|
| CLAIRE "Excellent. A refrigerator full of ambition." | Autoironia para ninguém | respira antes, avaliando | 2/10, quase um murmúrio |
| CLAIRE "What?" | Atender sem cerimônia: é a Maya | imediata | 3/10, seca |
| CLAIRE "I assumed it was an emergency." | Defender a grosseria com lógica | — | 3/10 |
| CLAIRE "I had a salad." | Mentira confiante | — | 3/10 |
| CLAIRE "Recently." | A confiança vacila | micro-hesitação antes | 3/10 |
| CLAIRE "Monday." | Rendição (o "Claire." da Maya a obrigou) | 1 s de silêncio antes | 2/10, culpada |
| CLAIRE "Time is a social construct." | Dignidade absurda | queixo levantado; sem pausa | 4/10 |
| CLAIRE "Good night." | Carinho escondido na secura | quase-sorriso | 2/10 |
| CLAIRE "Finally." | Alívio banal | expiração longa antes | 2/10 |
| MAYA (V.O.) | Mesmo registro da SC001: rápida, irônica, carinhosa | o riso depois de "social construct" é solto e curto | 5/10 |

## Riscos de geração

| # | Risco | Planos | Solução |
|---|---|---|---|
| R1 | Fala fora de quadro (Maya V.O.) | SH14–SH18 | P16: gerar a voz de Maya à parte e usar só o áudio (ver a pendência) |
| R2 | Duas falas de Claire com pausas de escuta no mesmo plano | SH16 | Se o H3 não segurar as pausas, dividir em 3 gerações (uma fala cada) e montar com o V.O. de Maya entre elas |
| R3 | Telas de celular com texto | SH05, SH12, SH19, SH22 | Tela neutra na geração; texto composto na pós (regra do estúdio) |
| R4 | Câmera dentro da geladeira | SH07 | Se a geração falhar, trocar por MS lateral com a porta aberta e a luz fria no rosto. **Pede aprovação** (é uma escolha de linguagem) |
| R5 | Deriva de cabelo na caminhada | SH06, SH23 | Regra L1 |
| R6 | Chave torta (objeto pequeno + dedo) | SH04 | Regra L8: testar primeiro (os dedos funcionaram na SC001) |
| R7 | Ligação com o primeiro quadro travado da SC003 | SH23 | Usar o primeiro keyframe da SC003 como **último quadro** da SH23 (P12) |

## Para aprovação
- (a) **O que aprovar:**
  1. Decupagem de 23 planos (~1:26) com câmera **totalmente estática**.
  2. Câmera **dentro da geladeira** (SH07).
  3. **Trench preto (L3)** como casaco da Claire.
  4. **Sem música** até a batida.
  5. A recomendação da **P16** para a voz da Maya.
- (b) **Pendências que bloqueiam:**
  - **P12:** os 18 keyframes da SC003 travam a entrada (SH01–SH04, SH22, SH23) e definem se a Claire está de blazer em casa.
  - **P16:** bloqueia o áudio de SH13–SH18.
  - A cozinha (SH05–SH21, menos o áudio da Maya) pode ser gerada já.
- (c) **Próximo passo:** receber os keyframes da SC003 e decidir a P16. Enquanto isso, gerar os **plates N e S** e o **keyframe-mestre da Claire na cozinha**, e trazer para a checagem de continuidade.
