# Pacote de geração no H3 — S01E01 · SC002 "A Perfectly Ordinary Night"

**Plataforma:** buzzy.now · **Modelo:** MiniMax-H3 (padrão, o mesmo da SC001) · **Data:** 2026-11-12
**Base:** decupagem SC002 V01 (APROVADA) + 16 keyframes aprovados no ChatGPT + método de fala A (P-13).
**Status:** pronto para uso. Os nomes dos keyframes serão confirmados quando o ZIP for checado aqui.

## Antes de cada geração (sempre)
1. **Proporção 16:9.** O teste de áudio saiu em 21:9: confira sempre.
2. **Resolução:** 480p só para teste; o plano aprovado é gerado na **maior resolução disponível**.
3. **Duração:** o mínimo da plataforma (4–5 s), a não ser que a tabela diga outra coisa. O corte fino é feito na montagem.
4. Nos prompts, troque cada `@NOME` pela **etiqueta do arquivo**, no meio do texto (digite `@` e escolha o arquivo na lista).
5. **Uma fala por geração** sempre que possível. Se o lip-sync falhar num plano com várias falas, divida.
6. Aprovou? Salve como `S01E01_SC002_SH##_V##.mp4` e anote no manifesto.

## Arquivos de referência (ter à mão)
| Etiqueta sugerida | Arquivo |
|---|---|
| `@ID_CLAIRE` | `02_CHARACTERS/CLAIRE_BENNETT/claire_ref-SC001_t04s.jpg` |
| `@VOZ_CLAIRE` | `06_GENERATED_ASSETS/VOICES/claire_bennett_voice-ref_v02.wav` |
| `@ID_MAYA` | `02_CHARACTERS/MAYA_REED/maya_ref-SC001_t82s.jpg` |
| `@VOZ_MAYA` | `06_GENERATED_ASSETS/VOICES/maya_reed_voice-ref_v02.wav` |
| `@KF-…` | o keyframe aprovado do plano (`S01E01_SC002_KF-…`) |

## Dois modos
- **SF = Start & end frame:** planos **sem fala**. Sobe o keyframe como **primeiro quadro**.
- **OR = Omni Reference:** planos **com fala**. Sobe o keyframe + `@ID_CLAIRE` + `@VOZ_CLAIRE`.

**Frase final de todo prompt com Claire:** *Her face, dark brown wavy hair with curtain bangs, wine-red lipstick and gold jewelry stay exactly the same. Natural hand anatomy. No on-screen text. No music.*

---

## Planos

### SH01 · SF · keyframe `KF-C01` · 5 s
> Static camera. The woman finishes stepping in through the front door and closes it behind her, the large black leather bag on her shoulder, her black trench coat damp at the shoulders. Calm, tired, composed. Warm amber lamp light. Sound: muffled rain, the door closing, footsteps. Her hair stays dark brown, long and wavy.

### SH02 · SF · keyframe `KF-INS-KEYS` · 4 s
> Static camera, extreme close-up. A woman's hand with thin gold rings and a black-strap watch enters the frame and drops her keys into the small ceramic dish, then withdraws. Warm lamp light. Sound: keys on ceramic.

### SH03 · SF · keyframe `KF-C02` · 5 s
> Static camera. She finishes hanging her damp black trench coat and black blazer on the wall hook beside the door, smoothing the coat once with her hand. She wears a fitted black long-sleeve top. Warm amber light. Sound: fabric, distant rain.

### SH04 · SF · keyframe `KF-INS-KEYS` · 4 s
> Static camera, extreme close-up. One key sits slightly crooked in the ceramic dish. A single finger enters the frame and nudges it until it is perfectly aligned with the others, then withdraws. Sound: a tiny metallic click.

### SH05 · ⚠️ falta keyframe
O pacote do ChatGPT não tem o **celular na mão de Claire na entrada**: o `KF-INS-PHONE` é o celular sobre o mármore da cozinha, e usá-lo aqui quebraria a geografia. **Gerar no mesmo chat da SC002** o keyframe **KF-INS-PHONE-HAND**:
> Close-up of a woman's hand with thin gold rings and a white-dial watch with a black strap holding a black smartphone at an apartment entrance at night, screen lit plain bright white with no text or icons; dark wood console and warm lamp blurred behind. 16:9, photorealistic.

Depois, SF · 4 s:
> Static camera, close-up. The phone in her hand vibrates once; the bright white screen stays plain. Sound: a short phone buzz.

### SH06 · SF · keyframe `KF-C03` · 5 s
> Static camera, wide shot from behind. She walks away from camera along the wall toward the white marble kitchen island; rain streaks down the floor-to-ceiling windows ahead, the blue Manhattan skyline beyond. She stays small in the frame. Her hair stays dark brown, long and wavy. Sound: footsteps, rain on glass growing slightly louder.

### SH07 · SF · keyframe `KF-C04` · 4 s
> Static camera from inside the refrigerator. She opens the door fully and looks in; cold white fridge light falls on her face, the warm kitchen behind her. Neutral, evaluating expression. Sound: fridge door opening, fridge hum.

### SH08 · SF · keyframe `KF-INS-FRIDGE` · 4 s
> Static camera. The open refrigerator contents in cold white light; nothing moves except a faint condensation shimmer. Sound: fridge hum.

### SH09 · OR · `@KF-C05` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 5 s
> Use @KF-C05 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium close-up, cold white refrigerator light on her face, warm kitchen behind her. She studies the contents with a perfectly straight face and a dry flicker of self-irony, then says quietly to herself: "Excellent. A refrigerator full of ambition." Use @VOZ_CLAIRE only as the reference for her voice. Sound: fridge hum. *(+ frase final)*

### SH10 · SF · keyframe `KF-INS-PASTA` · 4 s
> Static camera, close-up in cold fridge light. Her hand turns the plastic pasta container to read the small date label, pauses, then lowers it. Sound: plastic.

### SH11 · SF · keyframe `KF-C04` · 4 s
> Static camera from inside the refrigerator. She puts the pasta container back on the shelf and closes the door; the frame goes dark as the door shuts. Sound: fridge door closing; a phone starts ringing.

*(Ajuste de encenação: a SH11 reaproveita a câmera de dentro da geladeira, e a porta fechando escurece o quadro. Isso dá um corte cômico natural para o celular tocando e dispensa um keyframe novo.)*

### SH12 · SF · keyframe `KF-INS-PHONE` · 4 s
> Static camera. The phone on the white marble counter vibrates with an incoming call; the bright white screen stays plain. Warm pendant light. Sound: ringtone.

### SH13 · OR · `@KF-C06` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> Use @KF-C06 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium shot at the marble kitchen island, rain on the windows behind her. She taps the phone on the counter to answer on speaker and says flatly: "What?" Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH14 · OR · `@KF-C07` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 5 s
> Use @KF-C07 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium close-up. She listens to the phone on the counter for a moment, then answers, slightly defensive: "I assumed it was an emergency." Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH15 · SF · keyframe `KF-C07` · 5 s
> Static camera, medium close-up. She listens to the phone on speaker and says nothing; her eyes slide guiltily toward the refrigerator, then back. Sound: rain only, no dialogue.

### SH16 · OR · `@KF-C07` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 8 s *(ou 3 gerações de 4 s)*
> Use @KF-C07 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium close-up. She answers a friend on speakerphone with increasingly short, evasive replies, pausing to listen between them: "I had a salad." (pause) "Recently." (longer pause, guilty) "Monday." Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH17 · OR · `@KF-C08` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> Use @KF-C08 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, close-up, chin slightly raised. Perfectly dignified, she says deadpan: "Time is a social construct." Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH18 · OR · `@KF-C06` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 5 s
> Use @KF-C06 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium shot. An almost-smile tugs at her mouth as she listens; she says softly "Good night." and ends the call with one tap on the phone. Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH19 · SF · keyframe `KF-INS-PHONE` · 4 s
> Static camera. The phone on the marble counter lights up once with a notification; the bright white screen stays plain. Sound: notification chime.

### SH20 · OR · `@KF-C07` + `@ID_CLAIRE` + `@VOZ_CLAIRE` · 4 s
> Use @KF-C07 as the opening frame and composition, and @ID_CLAIRE as her identity. Static camera, medium close-up. She exhales, relieved, says softly "Finally." and reaches for a glass of water on the counter. Use @VOZ_CLAIRE only as the reference for her voice. Sound: rain. *(+ frase final)*

### SH21 · SF · keyframe `KF-C09` · 4 s
> Static camera, medium close-up. She holds the glass of water; a quiet knock sounds and she freezes mid-motion, her eyes turning to the left of the frame, toward the apartment entrance. Sound: a soft knock at the door, rain.

### SH22 · SF · keyframe `KF-INS-PHONE` · 4 s
> Static camera. The phone on the marble counter lights up again; the bright white screen stays plain. Sound: notification chime.

### SH23 · SF · início `S01E01_SC003_KF-C10_V03` → fim `S01E01_SC003_KF-C-DOOR_V01` · 5 s
> Static camera, wide shot from the kitchen looking toward the front door at the far end. She sets down her glass and walks away from camera toward the door, smaller with each step. Her hair stays dark brown, long and wavy. Sound: footsteps, rain.

Junção pronta (2026-11-13): use o C10 V03 e o C-DOOR da SC003.

---

## Voz de Maya (V.O.): planos-fonte, usar SÓ o áudio
Modo **OR** · `@ID_MAYA` + `@VOZ_MAYA` · 16:9 · fundo neutro. O vídeo é descartado; na mixagem, o áudio recebe EQ de alto-falante de celular.

Prompt-base (troque só a fala):
> Use @ID_MAYA as her identity. Static camera, medium close-up of the woman at home at night holding a phone to her ear, warm lamp light, plain dark background. She speaks with quick, warm, teasing irony: "[FALA]". Use @VOZ_MAYA only as the reference for her voice. No music.

| ID | Fala |
|---|---|
| MAYA-VO-01 | "That's a lovely way to greet someone." |
| MAYA-VO-02 | "It is. I'm checking whether you've eaten something that wasn't prepared by a restaurant." |
| MAYA-VO-03 | "When?" … "Claire." *(duas falas com pausa de ~1 s)* |
| MAYA-VO-04 | "It's Thursday." *(seguido de uma risada curta e solta)* |
| MAYA-VO-05 | "Good night, you terrifying woman." |

---

## Depois de gerar
Me mande os planos aprovados, ou um ZIP com eles. Eu confiro a continuidade entre os planos (cabelo, luz da mesma noite, figurino sem blazer, 16:9) e registro no repositório.
