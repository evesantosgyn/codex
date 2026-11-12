---
name: decupagem
description: Modo 4 (Produção com IA). Transforma uma cena de roteiro aprovada em decupagem técnica, com fichas de plano e prompts de geração em inglês no padrão do Estúdio GL AI. Use quando pedirem decupagem, shot list, storyboard, planos, keyframes ou prompts de uma cena (ex.: "decupa a SC001").
---

# Decupagem de cena

## Antes de começar (obrigatório)
1. Leia `SERIES_XXX/01_SERIES_BIBLE/registro-decisoes.md` e confirme que a cena está em um roteiro aprovado. Se não estiver, avise e pergunte se deve seguir como decupagem **proposta**.
2. Leia `pendencias.md` e liste as pendências que afetam esta cena. Não as resolva: marque os planos afetados como "depende de Pxx".
3. Leia o roteiro (`04_SCRIPTS/`) e a escaleta (função dramática, humor e intenção da cena).
4. Leia `continuidade.yaml`: traços fixos, looks e cronologia.
5. Leia a ficha da locação e **abra as pranchas `.webp`** da locação e das personagens presentes.
6. **Confira o material já aprovado** (vídeos em `06_GENERATED_ASSETS/VIDEO/` e análises em `05_STORYBOARDS/`) da última cena com as mesmas personagens e locação. **Material aprovado prevalece** sobre planta e prancha (regra L6).
7. Aplique `templates/checklist-pre-geracao.md` e as lições de `00_ESTUDIO/03_manual-producao-ia.md` §12: transição de figurino e objetos (L3), luz entre eixos (L2), deriva de cabelo em planos abertos (L1).
8. Se a cena for TRAVADA (ex.: SC003), as falas e ações são intocáveis. A decupagem só divide o que já existe.

## Processo
1. **Resumo da cena:** intenção dramática, estratégia visual, geografia (área da planta e eixo de 180°), padrão de luz, looks e pendências (formato em `templates/ficha-plano.md`).
2. **Lista de planos:** quebre a cena em planos curtos e controláveis. Uma ação principal por plano. Distribua as falas **literalmente** como no roteiro. Mantenha a soma das durações próxima da duração prevista da cena.
3. **Justifique a linguagem:** cada movimento de câmera tem motivo dramático; close-ups ficam nos momentos em que o rosto conta mais que as palavras; plano/contraplano para diálogos.
4. **Keyframes:** indique quais planos precisam de keyframe aprovado antes do vídeo (image-to-video).
5. **Prompts:** para cada plano, preencha `templates/prompt-plano.md` em inglês. Inclua as restrições negativas padrão e os traços fixos das personagens. Se a ferramenta alvo não estiver definida (P11), escreva no formato de campos genérico e diga que a adaptação de sintaxe fica pendente.
6. **Áudio:** para cada plano, fala, ambiência e SFX. Ao final, a direção de interpretação de cada fala (intenção, pausa, respiração).
7. **Prompts para a ferramenta real:** adapte ao MiniMax H3 conforme `00_ESTUDIO/04_manual-ferramentas.md` (duração mínima, imagem inicial e final, referências de imagem e de voz).
8. **Riscos de geração:** sinalize planos difíceis para IA (mãos manipulando objetos pequenos, como a árvore de 4 mm; líquidos, como o café derramado; texto em tela, como slides e celular; interação física entre personagens) e proponha alternativas de decupagem (inserts, cortes, ação fora de quadro).

## Saída
- Salve em `SERIES_XXX/05_STORYBOARDS/S01E0X_SC0XX_decupagem_V01.md`.
- Termine listando: (a) o que precisa de aprovação, (b) pendências que bloqueiam planos, (c) próximo passo sugerido.
- Use o padrão de IDs `S01E01_SC001_SH01_V01`. A numeração recomeça em cada cena (SH01, SH02…; decisão P07).
- Não avance para geração sem aprovação.
