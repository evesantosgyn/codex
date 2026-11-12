# Manual de Ferramentas — Estúdio GL AI

Versão 0.1 · 2026-11-12 · **Em construção** (ver P11 em cada série)

> Regra do estúdio: só é fato o que foi **verificado**. Cada especificação abaixo tem o seu nível de confiança indicado.
> Legenda: ✅ verificado no nosso material · 🔎 fonte secundária (sites de terceiros, conferir na documentação oficial) · ❓ a confirmar com o responsável

## Pipeline atual (decisão do responsável, 2026-11-12)

| Etapa | Ferramenta | Status |
|---|---|---|
| Geração de vídeo | **MiniMax H3 (Hailuo 3)** | APROVADO |
| Consistência de personagem | **LoRA** (por personagem) | APROVADO; modelo-base, onde roda e quais personagens já têm LoRA ❓ |
| Imagens / keyframes | ❓ (provavelmente o mesmo ambiente das LoRAs) | A confirmar |
| Voz / diálogo | ❓ áudio nativo do H3 ou ferramenta separada | A confirmar |
| Montagem | ❓ (candidatas: DaVinci Resolve, Premiere Pro) | A confirmar |
| Legendas | ❓ (candidata: Whisper) | A confirmar |
| Orquestração | ComfyUI (Bíblia V2.1) | APROVADO; workflows ❓ |

## MiniMax H3 (Hailuo 3)

### Especificações
| Item | Valor | Confiança |
|---|---|---|
| Duração por geração | Inteiros de **4 ou 5 até 15 s**, conforme a plataforma | 🔎 |
| Resolução | **2K** (~1440 px no lado curto); 768p varia por provedor | 🔎 |
| Modos | Text-to-video; **image-to-video** (anima uma imagem fixa ou **primeiro + último quadro**) | 🔎 |
| Referências | Até **9 imagens + 3 vídeos + 3 áudios** (12 arquivos) por tarefa | 🔎 |
| Proporções | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 (no i2v, segue a imagem) | 🔎 |
| Áudio | **Áudio estéreo nativo** gerado junto com o vídeo | 🔎 |
| Saída real do nosso teste SC001 | 3868 × 2160, 30 fps, planos de até ~7,3 s, com falas | ✅ (provavelmente upscale/reenquadramento depois do H3 ❓) |

Fontes (secundárias): [Artlist](https://help.artlist.io/hc/en-us/articles/38170376973853-MiniMax-H3-Hailuo-3) · [Runway](https://runway.com/product/models/minimax-h3) · [Morphic](https://morphic.com/resources/models/minimax-h3) · [ofox.ai](https://ofox.ai/docs/develop/models/hailuo)

### Como adaptar o padrão de prompt do estúdio ao H3
O padrão de campos (`templates/prompt-plano.md`) continua sendo a ficha de trabalho. Na hora de gerar:

1. **Imagens de entrada:** keyframe aprovado do plano (gerado com as LoRAs) como **primeiro quadro**. Quando o fim do plano importa para o corte (ex.: Claire chegando ao elevador), usar também um **último quadro**.
2. **Referências:** usar os slots de imagem para fixar a identidade: Identity Pack da personagem (frontal + 3/4), plate da locação e, quando houver, um quadro do plano anterior para continuidade. Máximo 9.
3. **Texto do prompt:** converter os campos num parágrafo em inglês, nesta ordem: *tamanho do plano e composição → quem está em quadro e onde → ação (uma só) → atuação facial → movimento de câmera (ou "static camera") → luz e cor → fala exata entre aspas, com quem fala → ambiência*. Deixar de fora do texto o que a imagem de entrada já garante (rosto, roupa, cenário): repetir descrição física pode puxar a identidade para longe da LoRA.
4. **Restrições negativas:** escrever como frases positivas no texto ("the camera stays static", "her hair remains dark brown") se a plataforma usada não tiver campo de prompt negativo ❓.
5. **Duração:** valores inteiros. A decupagem pode pedir 2–3 s, mas **o H3 gera no mínimo 4–5 s**: gerar no mínimo e **cortar na montagem**. Vantagem: sobra material para ajustar o timing da comédia.
6. **Diálogo:** se as vozes vierem do áudio nativo do H3 ❓, a fala exata vai no prompt; se vierem de ferramenta separada, gerar sem fala e fazer o lip-sync depois.

### Riscos observados no teste da SC001 ✅
- **Deriva de cor de cabelo** em planos de corpo inteiro e caminhada (Claire ficou acobreada). Mitigação: referência frontal da personagem + quadro anterior como referência; descrever "dark brown hair" no texto **só** nesses planos.
- **Luz diferente entre plano e contraplano** (fundo noturno × pôr do sol). Mitigação: plate de locação único por eixo e correção de cor.

## LoRA (consistência de personagem)
❓ **A documentar:** modelo-base (ex.: SDXL, Flux…), onde treina e roda (ComfyUI?), quais personagens já têm LoRA, peso usado, palavra-gatilho, dataset (veio dos Identity Packs?) e versões.

Regra do estúdio: **uma LoRA por personagem, versionada** (`claire_bennett_lora_v01`…). Rostos travados (Claire, Olivia) só mudam de LoRA com aprovação.
