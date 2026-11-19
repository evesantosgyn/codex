# Pacote ChatGPT — S01E02 · SC008 "Half the Truth"

> **Uso:** **chat novo** dentro do Projeto. O briefing fixo já está nas instruções do Projeto. Cole **tudo abaixo da linha** e anexe as imagens R1–R5.

---

# PACOTE DE CENA — THE SPACE BETWEEN US · S01E02 "FAMILIAR STRANGERS" · SC008 "HALF THE TRUTH"

## 1. Onde estamos
- **Série:** *The Space Between Us*, comédia romântica adulta com drama, em Manhattan.
- **Quando e onde:** terça à **noite**, dentro da van de produção do documentário, estacionada numa rua tranquila.
- **A cena:**
  - June Park, a produtora, está no banco do motorista; Olivia Hayes, no do passageiro, olha para o nada;
  - June pergunta se ela contou a Claire. Olivia conta só uma parte da verdade;
  - June diz apenas "About that.", e Olivia, virada para a janela, admite: "About that.";
  - June liga o motor.
- **Tom:** curto, seco, triste. Sem comédia. Olivia está vazia e culpada; June, gentil.
- **Visual:** as duas com leve câmera na mão, planos próximos, rostos meio na sombra.

## 2. Imagens de referência para ANEXAR
Pasta do repositório `evesantosgyn/codex`: `SERIES_001_THE_SPACE_BETWEEN_US/`
| Anexo | Arquivo | Para quê |
|---|---|---|
| **R1** | `03_LOCATIONS/VAN_PRODUCAO/van_prancha.png` | **A van:** bancos da frente, para-brisa com a rua escura, bancada com o laptop aceso, caixas, cabos, tripé na parede |
| **R2** | `02_CHARACTERS/OLIVIA_HAYES/olivia_ref-SC003_KF-O1.png` | **Rosto de Olivia** (pinta) |
| **R3** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC007_KF-O10_V02.png` | **Olivia hoje:** suéter marrom em V, coque |
| **R4** | `02_CHARACTERS/JUNE_PARK/june_ref-SC005_KF-J1.png` | **Rosto de June** |
| **R5** | `06_GENERATED_ASSETS/IMAGES/S01E02_SC005_KF-J2_V02.png` | **June hoje:** overshirt areia, camiseta branca, crachá, relógio preto |

## 3. Personagens (traços FIXOS + look de hoje)
**OLIVIA HAYES**, 33.
- **Rosto:** igual a R2. **Coque bagunçado loiro-escuro** com mechas soltas e **UMA pinta pequena logo abaixo do lábio inferior, do LADO ESQUERDO dela**.
- **Look:** **suéter de tricô marrom com decote em V** (R3) e jeans; **SEM relógio**.
- **No banco do PASSAGEIRO** (à direita do quadro).

**JUNE PARK**, 34.
- **Rosto:** igual a R4. **Cabelo castanho-escuro quase preto, liso, na altura da clavícula.**
- **Look:** **overshirt creme (tom areia)** sobre **camiseta branca**, **crachá de produção num cordão preto** (sem texto legível) e **relógio de pulseira de couro preta no pulso ESQUERDO** (R5).
- **No banco do MOTORISTA** (à esquerda do quadro).

## 4. Cenário, eixos e luz
- **A van de R1:** volante à esquerda (EUA); atrás dos bancos, a bancada com o laptop aceso (programa de edição, **tela sem texto legível**), as caixas de equipamento, os cabos e um tripé de luz preso na parede.
- **Pelo para-brisa:** a rua escura com os postes de luz quente.
- **Eixo:**
  - June olha para a **DIREITA** (Olivia);
  - Olivia olha **para frente** (para-brisa) ou, no fim, para a **janela do lado DIREITO**.
- **Luz:** **noite**. A luz fria e laranja dos postes entra pelas janelas, e o laptop dá um brilho quente atrás. **Rostos meio na sombra**: escuro, mas com os rostos legíveis.
- **Sem texto legível** em nada.

## 5. Keyframes (gerar nesta ordem)

### Etapa 1 — As duas (aprovar o J3 e o O11 antes de seguir)
| ID | Refs | Prompt |
|---|---|---|
| **KF-VAN-WS** | R1, R3, R5 | Inside the production van from R1 at night, seen from behind the front seats. On the LEFT, in the driver's seat, June (R5) closes a small black camera case on her lap. On the RIGHT, in the passenger seat, Olivia (R3) stares ahead through the windshield at nothing. Through the windshield: a dark, quiet street with warm streetlights. At the edge of the frame, the work bench with a glowing laptop (screen not readable). Faces half in shadow. 16:9, 28mm. |
| **KF-J3** | R4, R5, R1 | Medium close-up, subtle handheld: June in the driver's seat of the van at night, looking toward the **RIGHT** at her friend in the passenger seat; quiet, dry, kind; she already knows the answer. Straight dark hair at collarbone length, sand-cream overshirt over a white T-shirt, production badge on a black lanyard (no readable text). Cool streetlight from the window on one side of her face, a faint warm glow from the laptop behind. 16:9, 85mm. |
| **KF-O11** | R2, R3, R1 | Medium close-up, subtle handheld: Olivia in the passenger seat of the van at night, staring straight ahead through the windshield, empty, tired, guilty; half her face in shadow, the other half lit by a warm streetlight. Brown knit V-neck sweater, messy dark-blond bun, ONE beauty mark below her lower lip on her LEFT side, no wristwatch. 16:9, 85mm. |

### Etapa 2 — Variação e insert
| ID | Base | Prompt |
|---|---|---|
| **KF-O12** | KF-O11 | **Editar:** same image; Olivia has turned her head toward the passenger window on the RIGHT, looking out at the dark street; we see more of her cheek, her ear and her bun than her face; the streetlights reflect softly on the glass. |
| **KF-INS-KEY** | R5, R1 | Close-up in the dark van: June's hand (black leather-strap watch on her LEFT wrist, sand-cream sleeve) turning the key in the ignition; the dashboard lights just beginning to glow blue and amber. No readable text on the dashboard. 16:9, 100mm. |

## 6. Autochecagem OBRIGATÓRIA em TODAS as imagens
`[ID] · rosto (Olivia = R2; June = R4) ✔/✖ · cabelo (Olivia coque loiro; June liso escuro) ✔/✖ · figurino ✔/✖ · relógio (June preto, pulso esquerdo; Olivia sem) ✔/✖ · pinta (Olivia, UMA) ✔/✖ · posições (June motorista à esquerda; Olivia passageiro à direita) ✔/✖ · direção do olhar ✔/✖ · noite com rostos legíveis ✔/✖ · sem texto legível ✔/✖ · observação: …`
Se algum item for ✖, diga e proponha a correção **antes** de seguir.

## 7. Critérios de aprovação
- **June:** rosto igual a R4, overshirt areia, camiseta branca, crachá e relógio preto; motorista, à **esquerda**, olhando para a **direita**.
- **Olivia:** rosto igual a R2, uma pinta, suéter marrom e coque, **sem relógio**; passageiro, à **direita**.
- **A van de R1**, à noite: escura, mas com os **rostos legíveis**.
- **Nenhum texto legível**, nem no laptop, nem no painel, nem no crachá.
