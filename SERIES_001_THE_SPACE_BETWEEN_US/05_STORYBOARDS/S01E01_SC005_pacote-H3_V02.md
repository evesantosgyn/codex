# Pacote de geração no H3 — S01E01 · SC005 "The Woman Who Came Back" · V02 (REFAÇÃO)

**Status:** ✅ APROVADO (2026-11-18, V62) · **Data:** 2026-11-18
**Substitui:** `S01E01_SC005_pacote-H3.md` (V01) só nos blocos de interpretação, nas direções por fala e na montagem. **Roteiro, falas, planos e keyframes da V01 continuam**, mais um keyframe novo, o KF-O1-B.
**Motivo:** a versão gerada (`sc005.mp4`, 1:23) ficou sem emoção. Olivia está alerta e neutra, e as piadas de June saem chapadas. Análise abaixo.

## 1. Diagnóstico da versão gerada

**Imagem (frames de cada plano):**
- **Olivia:** o KF-O1 é o quadro inicial de 13 falas e a mostra **de olhar direto em June, postura ereta e atenta**. O vídeo herda essa energia, por isso Olivia nunca olha pela janela nem para a xícara. Só nos planos do O2 (queixo na mão, SH31–SH37) aparece algo pensativo.
- **June:** a cara está boa, viva e seca. O problema dela é a voz.
- **Continuidade:** em 6 planos de June (SH04, SH15, SH28, SH30, SH32, SH34), o fundo é **a janela com a rua**, e não o interior do café. A decupagem pede o balcão atrás de June, então o fundo pula a cada corte.

**Áudio (medição de entonação: variação de altura da voz por fala, em semitons):**

| | Variação média | Leitura |
|---|---|---|
| June | ~8 st, mas **3,8–5 st nas piadas** ("Then what did I just say?", "You went to see her", "Did you apologize?", "One disaster at a time") | Fala natural expressiva fica em 8–12 st. As piadas saíram **mais chapadas que o resto** |
| Olivia | ~6 st, com **3–4 st** nas falas-chave ("I didn't get that far", "I know that too") | Chapada, e com quase **a mesma altura média de June** (175 Hz × 173 Hz): as duas vozes soam iguais |

- **Ritmo:** "I went to her apartment" sai em ~1,3 s. Num tom pausado, seria 2,5–3 s.
- **Duração:** a cena montada tem 1:23, contra 1:39 do animatic. As pausas foram cortadas.

**A causa nos prompts da V01:**
1. O bloco de June pedia literalmente *"dry, quick… deadpan"*, e o modelo entregou voz **sem entonação**. Deadpan tem de estar na cara, não na voz.
2. O bloco de Olivia pedia *"warm… quiet and unhurried"*, sem nenhum estado emocional. As direções de fala eram leves e cômicas: *"innocent"*, *"dodging"*, *"with a wry wince"*.
3. O keyframe de Olivia é neutro, e no modo OR é ele que define a energia do plano.

**Uma ressalva sobre a tristeza "em todas as falas":** concordo, com uma nuance. Na primeira metade (SH05–SH27), a tristeza fica **por baixo**: Olivia faz piada e sorri, mas o sorriso não chega aos olhos. É humor como defesa. Na segunda metade (SH28–SH39), a tristeza vem à tona. Assim, o riso do SH27 continua funcionando, e a virada para "Did you tell her why you left?" ganha peso.

## 2. Keyframe novo: KF-O1-B (ChatGPT, Editar a partir do KF-O1)
> Same image, same framing, same clothes and light. Change only Olivia's expression and gaze: her eyes are lowered toward her coffee cup, slightly unfocused, lost in thought; her eyelids a little heavy, a faint tiredness and sadness around the eyes; her mouth relaxed, not smiling. Shoulders a bit softer, less upright. Keep her face, the ONE beauty mark below her lower lip on her left side, the messy bun, the window and the rainy street behind her exactly the same.

O **O1-B** substitui o O1 como quadro inicial de **todas as falas de Olivia** de SH07 a SH25. Ela começa olhando para baixo e ergue os olhos para June só quando fala. O O1 original fica para o SH11 (o sorriso) e o SH39 (o final).

## 3. Blocos novos

**Bloco de Olivia (OR):**
*Use @KF-… as the opening frame and composition, and keep @ID_OLIVIA's face (messy bun). Emotional state for the whole scene: last night she saw the woman she left seven years ago, and it went badly; under every line there is a quiet sadness she is trying to hide. Her eyes are tired and slightly unfocused; they drift down to her cup or out to the rainy window before and after she speaks, and she only half-meets June's eyes. Voice: warm, medium-low, slightly husky American; soft and low-energy, SLOWER than normal speech, with a small breath or hesitation before the line and endings that trail off. When she jokes or smiles, the smile does not reach her eyes. Never bright, never quick, never theatrical; no tears.*

**Bloco de June (OR):**
*Use @KF-… as the opening frame and composition, and keep @ID_JUNE's identity. June speaks in a dry, medium-low American voice with sharp comic timing. Her FACE is deadpan, but her VOICE is not flat: like a seasoned comedian underplaying a joke, she takes a tiny pause before the punchline and puts a light, ironic stress on the key word. On the punchline her eyebrows lift a millimeter and the corner of her mouth almost moves. Under the dryness, warm affection for her friend.*

**Fundo dos planos de June (anexar à frase final):** *Behind June: the café interior (counter, espresso machine, pastry case, warm light), NOT the window or the street.*

## 4. Direção por fala (substitui a coluna Prompt da V01)

| Plano | KF | Fala | Direção nova (depois do bloco) |
|---|---|---|---|
| SH04 | J1 | JUNE "We have access…" | Reading from her laptop, brisk and businesslike, a quick list, with a tiny weary stress on "today". |
| SH05 | O1-B | — | Olivia, eyes on the rainy window, gives a vague nod that comes a beat too late. |
| SH06 | J1 | JUNE "Olivia?" | She looks up over the laptop: "Olivia?", rising, patient, already knowing. |
| SH07 | O1-B | OLIVIA "I'm listening." | Pulled back from her thoughts a beat late, eyes lifting slowly from the cup; soft: "I'm listening." |
| SH08 | J1 | JUNE "Then what did I just say?" | Sweetly, like a teacher who already knows the answer: "Then what did I just say?" |
| SH09 | O1-B | OLIVIA "Something about architecture." | A tired, half-hearted guess, eyes drifting away: "Something… about architecture." |
| SH10 | J1 | JUNE "Remarkable. You heard an entire noun." | "Remarkable." A beat. Then, with ironic stress, stretching the word: "You heard an ENTIRE noun." |
| SH11 | O1 | — | Olivia smiles faintly despite herself; the smile does not reach her eyes. |
| SH13 | J1 | JUNE "You went to see her." | She drops the joke; not a question, quiet and certain: "You went to see her." |
| SH14 | O1-B | OLIVIA "Who?" | She looks up slowly; a weak attempt at innocence that convinces no one: "Who?" |
| SH15 | J1 | JUNE "The woman you've been pretending not to think about since we landed." | Patient, precise, enjoying each clause a little: "The woman you've been pretending not to think about… since we landed." |
| SH16 | O1-B | OLIVIA "That's a very long description." | A faint, sad half-smile, eyes back on her cup: "That's a very long description." |
| SH17 | J1 | JUNE "Is it inaccurate?" | Eyebrow up, light: "Is it… inaccurate?" |
| SH19 | O1-B | OLIVIA "I went to her apartment." | A breath first; quietly, eyes on the cup, slowly: "I went to her apartment." |
| SH20 | J1 | JUNE "And?" | Leaning in a little, gentle: "And?" |
| SH21 | O1-B | OLIVIA "She opened the door." | The memory replaying behind her eyes; slow: "She opened the door." |
| SH22 | J1 | JUNE "Promising." | Mock-encouraging, a small upward lilt: "Promising." |
| SH23 | O1-B | OLIVIA "She looked like she wanted to murder me." | Self-deprecating, a small sad laugh caught in the voice: "She looked like she wanted to murder me." |
| SH24 | J1 | JUNE "Less promising." | The same tune as "Promising", but lower and falling: "Less promising." |
| SH25 | O1-B | OLIVIA "She didn't close it immediately." | Almost to herself, eyes on the window; a fragile, stubborn hope: "She didn't close it… immediately." |
| SH26 | J1 | JUNE "A romantic triumph." | Mock-ceremonial, slower, eyebrows up, every word weighed: "A romantic… triumph." |
| SH27 | 2S | — | Olivia laughs despite herself, covering her mouth, and the laugh fades into something sadder; June allows a tiny smile. |
| SH28 | J2 | JUNE "Did you tell her why you left?" | No joke now; soft and careful: "Did you tell her why you left?" |
| SH29 | O1 | OLIVIA "No." | A pause; eyes drop; barely audible: "No." |
| SH30 | J2 | JUNE "Did you apologize?" | Gentle, already guessing the answer: "Did you apologize?" |
| SH31 | O2 | OLIVIA "I didn't get that far." | A long pause looking out the window; then, very quietly: "I didn't get that far." |
| SH32 | J2 | JUNE "You can't spend seven years…" | Honest, kind, unhurried; not lecturing: "You can't spend seven years rehearsing a conversation… and then expect the other person to follow your script." |
| SH33 | O2 | OLIVIA "I know." | A slow exhale; she looks down: "I know." |
| SH34 | J2 | JUNE "And the project?" | Lightly, as if changing the subject, but watching her: "And the project?" |
| SH35 | O2 | OLIVIA "What about it?" | Guarded, a touch too quick (the one defensive line): "What about it?" |
| SH36 | J2 | JUNE "You know there are old records we still need to review." | Carefully, choosing each word: "You know there are old records… we still need to review." |
| SH37 | O2 | OLIVIA "I know that too." | Slow push-in. Heavy, slow, the past surfacing in her eyes: "I know that too." |
| SH38 | J1 | JUNE "One disaster at a time, then." | Opening the laptop again, with a small affectionate sigh, light: "One disaster at a time, then." |
| SH39 | O1 | — | Olivia gives a small, tired smile and looks out at the wet street; the sadness stays. |

Os planos sem fala que não aparecem aqui (SH01–SH03, SH12 e SH18) seguem como na V01.

## 5. Montagem
- **Devolva as pausas.** A cena deve voltar para perto de **1:35–1:40**.
  - **Antes:** SH19, SH29, SH31, SH33 e SH37, com 0,8–1,5 s de silêncio antes da fala de Olivia.
  - **Depois:** o SH27 (o riso que apaga) e o SH37.
- **Primeira metade (SH06–SH26):** o pingue-pongue continua rápido do lado de June. **Olivia é sempre a mais lenta** do par, e esse contraste é a cena.
- **Vozes na conversão:** a de Olivia deve ficar **mais grave e mais lenta** que a de June. Hoje as duas têm quase a mesma altura. A conversão preserva a entonação da geração, então a emoção precisa vir do H3, não da edição.
- **Teste antes de gerar tudo:** refaça primeiro **SH10, SH19, SH26 e SH31** (duas piadas de June e duas falas tristes de Olivia) e avalie antes de gerar o resto.

## 6. Para aprovação
1. O diagnóstico, e a tristeza "por baixo" na primeira metade, "à tona" na segunda.
2. O **KF-O1-B** como quadro inicial das falas de Olivia.
3. Os **blocos novos** de Olivia e June e a direção por fala.
4. A correção do fundo de June (o interior do café).
5. As pausas de volta na montagem (~1:35–1:40).
