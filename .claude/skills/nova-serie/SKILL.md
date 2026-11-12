---
name: nova-serie
description: Modo 1 (Desenvolvimento). Abre uma nova série do Estúdio GL AI com as mesmas regras de criação e desenvolvimento da SERIES_001. Cria a pasta a partir de _MODELO_SERIE e conduz as primeiras etapas de aprovação. Use quando pedirem uma série nova, um novo projeto, nova propriedade ou "vamos criar outra série".
---

# Nova série

A SERIES_001 (*The Space Between Us*) é o **exemplo de referência** de como cada artefato deve ficar quando estiver completo. Consulte-a sempre que tiver dúvida de formato ou profundidade. **Não copie** dela personagens, premissa, segredo ou locações.

## Etapa 0 — Briefing (antes de criar arquivos)
Pergunte ou confirme, de forma objetiva:
1. Gênero principal e camadas (Bíblia Criativa §2).
2. Público e proposta emocional.
3. Formato: número de episódios e duração (Bíblia Criativa §7).
4. Restrições ou desejos do responsável (época, cidade, tom, referências de estilo).

## Etapa 1 — Alternativas de conceito (aprovação obrigatória)
Apresente **3 conceitos distintos**, cada um com título, logline, premissa, protagonistas em 2 linhas, conflito central, pergunta dramática da temporada e o motivo de a ideia sustentar uma temporada (ou recomende minissérie/filme). Avalie cada um pelos critérios do estúdio e indique o seu recomendado. **Pare e aguarde a escolha.**

## Etapa 2 — Criar a estrutura
Após a aprovação do conceito:
1. Código: o próximo número livre (`SERIES_002`, `SERIES_003`…). Pasta: `SERIES_NNN_TITULO_EM_MAIUSCULAS_COM_UNDERSCORES/`.
2. Copie `_MODELO_SERIE/` para a nova pasta (`cp -r`) e substitua `{{TÍTULO}}`, `{{NNN}}` e `{{DATA}}`.
3. Renomeie `_MODELO_PERSONAGEM` e `_MODELO_LOCACAO` conforme forem criados (`NOME_SOBRENOME/`, `NOME_LOCACAO/`).
4. Registre o conceito aprovado em `registro-decisoes.md` (N01) e preencha `biblia-serie.md`.
5. Acrescente a série à tabela "Séries ativas" do `CLAUDE.md`.

## Etapa 3 em diante — seguir o fluxo do estúdio
Siga o "Fluxo de trabalho de uma série" do `CLAUDE.md` (itens 3 a 10), **parando para aprovação** em cada etapa criativa:
bíblia → protagonistas (ficha dramática + Identity Pack) → secundárias → temporada e arcos → escaleta → roteiro → `revisao-roteiro` → script lock → locações (Location Identity Pack + planta coerente) → `decupagem` → produção.

## Regras herdadas (valem para todas as séries)
- Cânone, travamentos, pendências e registro de decisões funcionam exatamente como na SERIES_001.
- Rostos só viram "TRAVADO" depois de o responsável confirmar que não reproduzem pessoa real identificável.
- Plantas precisam ser geometricamente coerentes. Se a imagem errar, corrija em texto na ficha.
- Toda contradição encontrada vira uma pendência numerada; nunca é resolvida em silêncio.
- Numeração de planos recomeça em cada cena; IDs `S01E01_SC001_SH01_V01`.
