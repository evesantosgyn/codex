# Template — Prompt de geração por plano

> Sempre em inglês. Adaptar à sintaxe da ferramenta alvo (ver `00_ESTUDIO/04_manual-ferramentas.md` quando existir).
> Antes de preencher: conferir `continuidade.yaml` (traços fixos + look da cena) e `pendencias.md`.

```
SHOT ID: S01E01_SC000_SH00_V01
CHARACTER REFERENCES: [personagem → arquivo canônico + look (ex.: claire_bennett L1)]
LOCATION REFERENCES: [locação → prancha + área da planta (ex.: escritorio_claire, mesa de Maya)]
DRAMATIC INTENT: [o que este plano precisa fazer o espectador sentir/entender]
SHOT SIZE AND COMPOSITION: [WS/MS/2S/MCU/CU/ECU/OTS · lente aproximada · posição na tela · eixo]
CAMERA MOVEMENT: [static / slow push-in / pan / handheld leve, com motivo dramático]
CHARACTER ACTION: [ação física simples e única por plano]
FACIAL PERFORMANCE: [microexpressão, direção do olhar, respiração]
LIGHTING AND COLOR: [padrão de luz da locação/período + variações]
DIALOGUE / AUDIO: [fala exata do roteiro travado ou "no dialogue" · ambiência · SFX]
DURATION: [segundos, dentro do limite verificado da ferramenta]
CONTINUITY REQUIREMENTS: [traços fixos, acessórios, objetos de cena, posição em relação ao plano anterior]
NEGATIVE CONSTRAINTS: [o que não pode aparecer: mudança de rosto, mãos deformadas, texto ilegível, objetos fora da ficha...]
TARGET GENERATION TOOL: [ferramenta + modo (image-to-video / text-to-video / keyframe)]
```

## Restrições negativas padrão do estúdio (incluir quando aplicável)
- no change in facial structure, eye color, hair color or length between shots
- no extra or missing fingers; natural hand anatomy
- no exaggerated gestures or theatrical acting
- no unmotivated camera movement
- no random props or wardrobe changes not listed in continuity
- no visible logos or brand names other than the in-world studio logo
- no on-screen text unless specified (e.g., phone screens, slides)
