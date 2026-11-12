# Manual de Ferramentas — Estúdio GL AI

Versão 0.1 · 2026-11-12 · **Em construção** (ver P11 em cada série)

> Regra do estúdio: só é fato o que foi **verificado**. Cada especificação abaixo tem o seu nível de confiança indicado.
> Legenda: ✅ verificado no nosso material · 🔎 fonte secundária (sites de terceiros, conferir na documentação oficial) · ❓ a confirmar com o responsável

## Pipeline atual (decisão do responsável, 2026-11-12)

| Etapa | Ferramenta | Status |
|---|---|---|
| Geração de vídeo | **MiniMax H3 (Hailuo 3)** | APROVADO |
| Consistência de personagem | **LoRA** (por personagem) | APROVADO; modelo-base, onde roda e quais personagens já têm LoRA ❓ |
| Imagens / keyframes | **ChatGPT (geração de imagem)**, com imagens de referência anexadas; **um chat novo por cena**, aberto com `00_ESTUDIO/briefing-chatgpt-keyframes.md` + o pacote da cena (`05_STORYBOARDS/..._pacote-chatgpt.md`) | APROVADO (2026-11-12) |
| Voz / diálogo | **Áudio nativo do MiniMax H3** (gerado junto com o vídeo) | APROVADO (2026-11-12) |
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

### Interface usada pelo estúdio (verificada por prints do responsável, 2026-11-12) ✅
- **Menu de tarefa:** Modo agente · **Gerador de vídeo** · Gerador de imagens · **Gerador de áudio**.
- **Modelo:** MiniMax-H3.
- **Modo de referência do vídeo:**
  - **Omni Reference**: sobe arquivos de referência (campo "Ref Video" e "Ref") e chama cada um no prompt com `@` (ex.: "referencie @video e troque o sujeito por @image").
  - **Start & end frame**: primeiro quadro (e, opcionalmente, último quadro).
- **Controles:** resolução (padrão 480p), duração (padrão 4s), proporção, custo em créditos por geração.
- ✅ O campo de referência **aceita áudio** (aparece como "Song / MP3"). ❓ Falta testar **como o H3 usa esse áudio**: (A) amostra de voz para falas novas, (B) faixa que a personagem dubla tal como está, ou (C) música de fundo. Teste descrito em "Teste de áudio" abaixo.
- ❓ A confirmar: os nomes exatos das referências depois do upload (`@image1`? `@image`?), se Start & end frame aceita referências extras, e as resoluções disponíveis acima de 480p.

### Teste de áudio (pendente)
Omni Reference · 480p · 4 s · 16:9. Subir `claire_ref-SC001_t04s.jpg` e `claire_bennett_voice-ref_v02.wav`. Prompt pedindo uma **fala nova** ("Excellent. A refrigerator full of ambition.") na voz do áudio.
- **Resultado A**, ela diz a fala nova na voz da Claire → método: referência de voz no prompt (o mais simples).
- **Resultado B**, ela dubla o conteúdo do arquivo ("I'm aware…") → método: **gerar antes o áudio de cada fala** (Gerador de áudio, com a voz da personagem) e subir esse áudio como a faixa que ela dubla.
- **Resultado C**, o áudio vira música de fundo, sem sincronia → o campo não serve para voz; a fala vem do áudio nativo descrito no prompt + correção de voz na pós.

### Qual modo usar em cada plano
| Tipo de plano | Modo | Por quê |
|---|---|---|
| Plano **com fala** de personagem | **Omni Reference**, com keyframe (@image) + referência de rosto (@image) + voz (@audio, se aceitar) | É o único modo que leva referência de voz e de identidade junto |
| Plano **sem fala** que precisa casar exatamente com o anterior ou o seguinte (junção entre cenas, caminhada até um ponto) | **Start & end frame** | Composição de início e fim garantidas |
| **Inserts** sem rosto (chaves, celular, geladeira) | **Start & end frame**, só com o primeiro quadro | Fidelidade ao keyframe aprovado |
| **V.O.** (personagem fora de quadro) | Testar o **Gerador de áudio** com a referência de voz; se não clonar a voz, usar planos-fonte no Omni Reference (P16) | Pode simplificar a P16 |
| Testes | 480p | Economiza créditos; o **final** sai na maior resolução disponível |

### Como adaptar o padrão de prompt do estúdio ao H3
O padrão de campos (`templates/prompt-plano.md`) continua sendo a ficha de trabalho. Na hora de gerar:

1. **Imagens de entrada:** keyframe aprovado do plano (gerado com as LoRAs) como **primeiro quadro**. Quando o fim do plano importa para o corte (ex.: Claire chegando ao elevador), usar também um **último quadro**.
2. **Referências:** usar os slots de imagem para fixar a identidade: Identity Pack da personagem (frontal + 3/4), plate da locação e, quando houver, um quadro do plano anterior para continuidade. Máximo 9.
3. **Texto do prompt:** converter os campos num parágrafo em inglês, nesta ordem: *tamanho do plano e composição → quem está em quadro e onde → ação (uma só) → atuação facial → movimento de câmera (ou "static camera") → luz e cor → fala exata entre aspas, com quem fala → ambiência*. Deixar de fora do texto o que a imagem de entrada já garante (rosto, roupa, cenário): repetir descrição física pode puxar a identidade para longe da LoRA.
4. **Restrições negativas:** escrever como frases positivas no texto ("the camera stays static", "her hair remains dark brown") se a plataforma usada não tiver campo de prompt negativo ❓.
5. **Duração:** valores inteiros. A decupagem pode pedir 2–3 s, mas **o H3 gera no mínimo 4–5 s**: gerar no mínimo e **cortar na montagem**. Vantagem: sobra material para ajustar o timing da comédia.
6. **Diálogo (decisão de 2026-11-12: áudio nativo do H3):** a fala exata do roteiro vai no prompt, entre aspas e atribuída a quem fala ("Claire says: …"). Nos planos com duas personagens, **uma fala por geração** sempre que possível.
7. **Voz consistente:** usar os slots de **referência de áudio** (até 3) com o **clipe canônico de voz** de cada personagem em quadro (ver "Voice Identity Pack" abaixo). Sem referência, o H3 pode inventar uma voz diferente a cada plano.

### Riscos observados no teste da SC001 ✅
- **Deriva de cor de cabelo** em planos de corpo inteiro e caminhada (Claire ficou acobreada). Mitigação: referência frontal da personagem + quadro anterior como referência; descrever "dark brown hair" no texto **só** nesses planos.
- **Luz diferente entre plano e contraplano** (fundo noturno × pôr do sol). Mitigação: plate de locação único por eixo e correção de cor.

## Voice Identity Pack (método com H3)
Como a voz nasce junto com o vídeo, a identidade vocal é garantida por **clipes de referência**, não por um "ID de voz":

1. Para cada personagem, escolher **2 a 3 falas aprovadas** (limpas, sem música, sem a outra personagem falando por cima), com ~5–10 s no total. Para Claire e Maya, a fonte é o **vídeo da SC001 já produzido**, depois de aprovado.
2. Exportar como WAV em `06_GENERATED_ASSETS/VOICES/<personagem>_voice-ref_v01.wav` e registrar no `continuidade.yaml` (campo `voz`).
3. Descrever o timbre por escrito (registro, ritmo, sotaque, textura) na ficha da personagem, para o caso de a referência falhar.
4. Toda geração com fala usa a referência de quem fala. Voz que derivar = tomada rejeitada (mesma regra do rosto).
5. **Olivia e June** ainda não têm voz definida: a primeira cena com fala de cada uma (SC003 para Olivia, SC005 para June) vai **fixar** a voz. Gerar e aprovar a voz antes de produzir a cena inteira.

❓ A confirmar com o uso real: se a plataforma onde o H3 roda aceita referências de áudio para clonar a voz do clipe (as fontes secundárias citam "3 audio references", mas não descrevem a fidelidade).

## LoRA (consistência de personagem)
❓ **A documentar:** modelo-base (ex.: SDXL, Flux…), onde treina e roda (ComfyUI?), quais personagens já têm LoRA, peso usado, palavra-gatilho, dataset (veio dos Identity Packs?) e versões.

Regra do estúdio: **uma LoRA por personagem, versionada** (`claire_bennett_lora_v01`…). Rostos travados (Claire, Olivia) só mudam de LoRA com aprovação.

## Ferramentas avaliadas e não adotadas

### Pollo.ai — "Pollo Cinema 1.0" (avaliada em 2026-11-12, sem teste pago)
- **Vista nos prints do responsável:** 4K, planos de 4–30 s, referência de imagem e de áudio, controles de cena (gênero, época, formato de câmera, lente, abertura, tamanho do plano, ângulo, movimento, iluminação). Custo: 42 créditos para 5 s em 480p.
- **Pesquisa (fontes secundárias, 🔎):** nenhuma avaliação específica do Cinema 1.0. Sobre a plataforma Pollo em geral, as avaliações citam deriva de rosto, cintilação e luz inconsistente, e lip-sync "good enough". O uso comercial é contraditório entre as fontes: o plano gratuito tem marca d'água e não é monetizável.
- **Decisão:** **não adotada agora.** Continuamos com o MiniMax H3, já validado na SC001. Reavaliar só para casos específicos (planos > 15 s ou finalização em 4K), com um teste único comparado a um plano já feito no H3. Se for adotada, as configurações de cena **não podem ficar em "Auto"**: viram um padrão fixo da série.
