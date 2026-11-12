# S01E01 · SC002 — Pacote de keyframes V01

**Status:** PROPOSTA · **Base:** decupagem SC002 V01 (APROVADA) · **Data:** 2026-11-12
**Quem gera:** o responsável, no gerador de imagem com as **LoRAs** (modelo-base a documentar, P11). **Quem confere:** Showrunner, com a skill `checagem-continuidade`, antes de cada imagem virar primeiro quadro no H3.

## Como usar este pacote
1. Gere **na ordem das etapas** (A → B → C → D). Cada etapa só começa quando a anterior estiver aprovada: os plates fixam o cenário que as personagens vão ocupar.
2. Formato: **16:9**, na maior resolução do gerador. Salve em `06_GENERATED_ASSETS/IMAGES/` com o ID do keyframe (ex.: `S01E01_SC002_KF-PLATE-N_V01.png`).
3. `<claire>` = palavra-gatilho da LoRA da Claire (substituir pela real). Use o peso habitual da LoRA.
4. **Referências de identidade** em toda imagem com Claire: `claire-bennett_identity-pack.webp` + `claire_ref-SC001_t04s.jpg` (quadro aprovado da SC001, fiel ao rosto e à cor do cabelo).
5. Me envie cada etapa; eu confiro e só então ela é aprovada.

## ⚠️ Decisão pendente que afeta a etapa C
**Look de Claire em casa:** ela **tira o blazer** junto com o casaco ao chegar (recomendado: em casa, desarmada, quando Olivia aparece), ou **mantém o blazer**? Os prompts trazem a variável `{HOME_LOOK}`:
- Tira o blazer → `a fitted black long-sleeve top, no blazer`
- Mantém → `a black tailored blazer over a black top`

## Etapa A — Plates de locação (sem personagens) · regra L2

**KF-PLATE-S · Entrada (eixo S), noite**
> Cinematic still, wide shot inside an elegant Manhattan apartment at night, looking toward the front entrance. A dark-stained solid wood front door with a bronze handle, closed. To its side, a dark wood console table with a warm table lamp, a stack of art books, a small round handmade ceramic dish, and a tall dark vase with red branches; above it a large round mirror with a thin bronze frame; a slim vertical wall sconce glowing warm. A minimalist black wall hook beside the door. Warm amber light, deep shadows, faint cool blue light spilling from the living room windows off-screen. Polished dark wood floor with soft reflections. Quiet, refined, empty. 16:9, 35mm lens, shallow depth of field, natural film grain.

**KF-PLATE-N · Cozinha (eixo N), noite com chuva**
> Cinematic still, wide shot of an elegant open kitchen in a high-rise Manhattan apartment at night. A white marble kitchen island in the foreground, dark cabinetry, a brushed gold faucet, a bowl of green apples; three amber glass pendant lights glowing above the island. Behind the island, floor-to-ceiling windows streaked with heavy rain, the Manhattan skyline glowing deep blue and gold through the wet glass. Warm amber interior light against cool blue city light. Empty, quiet, luxurious. 16:9, 28mm lens, natural film grain.

**Critério de aprovação (L2):** os dois plates parecem **a mesma noite, no mesmo apartamento**: mesmas madeiras e bronzes, a mesma temperatura âmbar, e chuva visível ou sugerida nos dois.

## Etapa B — Inserts (sem rosto)

| ID | Plano | Prompt |
|---|---|---|
| KF-INS-KEYS | SH02, SH04 | Extreme close-up of a small round handmade ceramic dish on a dark wood console, holding a set of keys neatly aligned, **except one key sitting slightly crooked**. A large black leather bag rests at the edge of frame. Warm lamp light, shallow depth of field, 16:9. |
| KF-INS-PHONE | SH05, SH12, SH19, SH22 | Close-up of a black smartphone lying on a white marble counter, its screen lit **plain bright white with no text or icons** (to be replaced in post). Warm amber pendant light, rain-blurred city bokeh in the background, 16:9. |
| KF-INS-FRIDGE | SH08 | Point-of-view shot into an open modern refrigerator at night: neatly aligned bottles of sparkling water, perfectly arranged vegetables in clear containers, one wedge of expensive cheese, a single clear plastic container of leftover pasta with a small handwritten date label (not legible). Almost nothing that resembles dinner. Cold white fridge light, 16:9. |
| KF-INS-PASTA | SH10 | Close-up of a woman's hand with thin gold rings and a black-strap watch holding a clear plastic container of leftover pasta in cold refrigerator light, turning it to look at a small date label (not legible). 16:9. |

## Etapa C — Claire (identidade) · regras L1 e L3

**Referências obrigatórias em todas:** Identity Pack + `claire_ref-SC001_t04s.jpg` + o plate do eixo.
**Identidade fixa (já vai em cada prompt):** long dark-brown wavy hair with curtain bangs, brown eyes, strong dark eyebrows, deep wine-red lipstick, small gold hoops, double gold necklace (small dark-red pendant and a round pendant), white-dial watch with black strap, thin gold rings.

| ID | Planos | Prompt |
|---|---|---|
| KF-C01 | SH01 | `<claire>`, a woman of 35, stepping through her front door into a dim elegant apartment entrance at night, closing the door behind her; she wears a **black trench coat with rain-darkened shoulders** over black tailored clothes, a **large black leather bag** on her shoulder. Long dark-brown wavy hair with curtain bangs, slightly damp at the ends; wine-red lipstick; gold hoops. Wide shot from inside, the console table, round mirror and red branches beside her. Warm amber lamp light. Calm, tired, composed. 16:9, 35mm. |
| KF-C02 | SH03 | `<claire>` at her apartment entrance at night, hanging her damp black trench coat on a black wall hook beside the door (if `{HOME_LOOK}` = no blazer: the blazer hangs with it); now wearing `{HOME_LOOK}`. Long dark-brown wavy hair with curtain bangs, wine-red lipstick, gold hoops, double gold necklace. Medium shot, warm amber light. 16:9, 50mm. |
| KF-C03 | SH06 | Wide shot from behind: `<claire>` wearing `{HOME_LOOK}` walking away from camera along the wall of a large elegant apartment toward a marble kitchen island; floor-to-ceiling rain-streaked windows ahead with the blue Manhattan skyline. **Her hair is dark brown, long and wavy.** Small in the frame, alone. Warm amber pendants, cool blue window light. 16:9, 24mm. |
| KF-C04 | SH07 | Medium shot **from inside an open refrigerator** looking out, framed by shelves with sparkling water bottles: `<claire>` wearing `{HOME_LOOK}` looking in, her face lit by cold white fridge light, the warm amber kitchen behind her. Long dark-brown wavy hair with curtain bangs, wine-red lipstick. Neutral, evaluating expression. 16:9, 28mm. |
| KF-C05 | SH09 | Medium close-up of `<claire>` in cold white refrigerator light, warm kitchen behind her, studying the contents with a perfectly straight face and a dry flicker of self-irony. Long dark-brown wavy hair with curtain bangs, wine-red lipstick, gold hoops, double gold necklace. 16:9, 50mm. |
| KF-C06 | SH11, SH13 | Medium shot of `<claire>` wearing `{HOME_LOOK}` standing at a white marble kitchen island at night, phone on the counter in front of her; behind her floor-to-ceiling rain-streaked windows and the blue Manhattan skyline. Three amber pendants above. Long dark-brown wavy hair with curtain bangs, wine-red lipstick, gold hoops, white-dial black-strap watch. Composed. 16:9, 35mm. |
| KF-C07 | SH14–SH16, SH18, SH20 | Medium close-up of `<claire>` at the marble kitchen island at night, looking down at a phone on the counter, listening. Warm amber pendant light on her face, blue rain-blurred city bokeh behind. Long dark-brown wavy hair with curtain bangs, wine-red lipstick, gold hoops, double gold necklace. Dry, guarded expression. 16:9, 50mm. *(Keyframe-mestre: as variações de expressão saem no H3.)* |
| KF-C08 | SH17 | Close-up of `<claire>`, chin slightly raised, perfectly dignified and faintly absurd, warm amber light, blue bokeh behind. Long dark-brown wavy hair with curtain bangs, wine-red lipstick, gold hoops. 16:9, 85mm. |
| KF-C09 | SH21 | Medium close-up of `<claire>` at the marble island holding a glass of water, frozen mid-motion, eyes turned **toward screen-left** (toward the apartment entrance). Warm amber light. Long dark-brown wavy hair with curtain bangs, wine-red lipstick. 16:9, 50mm. |
| KF-C10 | SH23 | Wide shot from the kitchen looking **south** down the length of the apartment toward the dark front door at the far end, the console lamp glowing beside it: `<claire>` wearing `{HOME_LOOK}` walking away from camera toward the door. **Her hair is dark brown, long and wavy.** Rain reflections on the dark wood floor. 16:9, 28mm. |

## Etapa D — Junção SC002 → SC003
O **último quadro da SH23** e o **primeiro quadro da SC003** são desenhados juntos, na decupagem nova da SC003 (próximo passo). Por isso o KF-C10 só é aprovado **junto** com o primeiro keyframe da SC003.

## Checagem que vou aplicar em cada imagem recebida
- Rosto igual ao Identity Pack e ao quadro da SC001 (t = 4 s); **cabelo castanho-escuro, não acobreado** (L1); franja presente.
- Batom vinho, argolas, colar duplo, relógio de pulseira preta no pulso certo, anéis.
- Figurino da etapa certa: trench molhado (C01), `{HOME_LOOK}` a partir da C02 (L3).
- Cenário igual ao plate aprovado do mesmo eixo; mesma noite, mesma chuva (L2).
- Telas de celular sem texto; nenhuma pessoa extra; nenhum logo.
