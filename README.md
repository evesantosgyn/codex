# Estúdio GL AI — Base do agente Showrunner

Repositório de conhecimento e operação do **Showrunner GL AI**, o agente central de desenvolvimento e produção do estúdio de séries sáficas com IA.

## Como usar
Abra este repositório no Claude Code. O arquivo `CLAUDE.md` é carregado automaticamente e transforma o Claude no Showrunner, com as regras, os 6 modos e o fluxo de aprovação do estúdio.

Exemplos de pedidos:
- "Revisa o roteiro do piloto" → skill `revisao-roteiro`
- "Decupa a SC001" → skill `decupagem`
- "Checa a continuidade dessas novas pranchas" → skill `checagem-continuidade`
- "Vamos criar uma série nova" → skill `nova-serie` (mesmas regras, a partir de `_MODELO_SERIE/`)
- "Aprovo a Planta A do escritório" → o agente registra em `registro-decisoes.md` e fecha a pendência

## Estrutura
```
CLAUDE.md                         ← instruções mestras do agente
00_ESTUDIO/                       ← manuais do estúdio (valem para todas as séries)
  01_manual-mestre.md
  02_biblia-criativa.md
  03_manual-producao-ia.md
  fontes/                         ← PDFs originais
templates/                        ← prompt de plano, ficha de plano, QC, avaliação
.claude/skills/                   ← nova-serie · decupagem · revisao-roteiro · checagem-continuidade
_MODELO_SERIE/                    ← modelo de pastas e documentos para cada série nova
SERIES_001_THE_SPACE_BETWEEN_US/
  01_SERIES_BIBLE/
    biblia-serie.md               ← premissa, tom, estrutura da temporada
    canone-segredo-olivia.md      ← V2.2 (cânone)
    registro-decisoes.md          ← o que está aprovado ou travado
    pendencias.md                 ← pendências abertas e resolvidas
    continuidade.yaml             ← traços fixos, looks e cronologia
  02_CHARACTERS/                  ← ficha + prancha de cada personagem
  03_LOCATIONS/                   ← ficha + pranchas de cada locação
  04_SCRIPTS/                     ← roteiro V3.1 (aprovado) + escaleta V2.1
  05_STORYBOARDS/ … 11_PERFORMANCE_REPORTS/
```

## Ainda falta
- `00_ESTUDIO/04_manual-ferramentas.md`: precisa dos frameworks, dos prompts de execução e dos workflows do ComfyUI.
- `00_ESTUDIO/05_distribuicao.md`: plano de distribuição e monetização.
- Os 18 keyframes travados da Cena 003.
- Voice Identity Packs.
- Pendências abertas: P11 (pipeline técnico) e P12 (materiais a receber).
