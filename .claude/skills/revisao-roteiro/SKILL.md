---
name: revisao-roteiro
description: Avaliação crítica de roteiro, escaleta ou cena no padrão de qualidade do Estúdio GL AI (6 dimensões ponderadas, meta 8/10). Use quando pedirem para revisar, avaliar, dar nota ou criticar um roteiro, ou antes de travar um roteiro para produção.
---

# Revisão de roteiro

## Preparação
1. Leia o roteiro alvo e a escaleta correspondente.
2. Leia `biblia-serie.md`, `canone-segredo-olivia.md` (ou o cânone equivalente da série), `continuidade.yaml` e `registro-decisoes.md`.
3. Leia `00_ESTUDIO/02_biblia-criativa.md`, seções 3 (regras de roteiro) e 8 (critérios).

## Avaliação
Preencha `templates/avaliacao-roteiro.md`:
- Dê uma nota de 0–10 por dimensão, **justificada com exemplos concretos** (cena e fala).
- Calcule a ponderada: dramática 25% · personagens e química 25% · diálogos 15% · ritmo 15% · originalidade 10% · viabilidade 10%.
- Meta: ≥ 8,0 e nenhuma dimensão < 6. **Não infle notas.** Uma ideia interessante não é motivo para aprovar.

## O que procurar
- Diálogos expositivos ou personagens que falam todas igual.
- Química declarada em vez de mostrada.
- Contradições com o cânone, a cronologia ou a continuidade visual (registre em `pendencias.md`).
- Cenas que não mudam nada (sem função dramática).
- Segredo prolongado artificialmente; mágoa usada como obstáculo conveniente.
- Humor que diminui o drama central, ou personagens secundárias reduzidas a alívio cômico.
- Viabilidade com IA: ações difíceis de gerar, excesso de personagens em quadro, interações físicas complexas, texto em tela.

## Regras
- **Conteúdo TRAVADO não recebe sugestões de reescrita.** Avalie, mas proponha ajustes só ao redor dele.
- Proponha soluções concretas (fala alternativa, corte, reordenação), não críticas vagas.
- A nota orienta, mas a decisão é do responsável pelo estúdio. Termine com um veredito recomendado e o que precisa de aprovação.
- Salve em `SERIES_XXX/04_SCRIPTS/<roteiro>_avaliacao_<data>.md`.
