# EP02 montado — análise de emoção (Olivia) · V01

**Status:** 🟡 PROPOSTA (2026-11-25), aguardando decisão · **Material:** corte do EP02 enviado pela responsável (Drive, 8:22, 3840×2160)
**Método:** o mesmo do EP01 e das referências:
- transcrição com tempo por palavra;
- falas alinhadas ao roteiro V1.2;
- velocidade, pausa antes de cada fala e variação de tom (semitons, percentil 5–95) por fala;
- quadros dos rostos nas falas-chave.

## 1. O que os números mostram
| | Olivia | Claire | Maya | June | Alvo (§13/§14) | Referências |
|---|---|---|---|---|---|---|
| Palavras por segundo (mediana) | **4,5** | 3,5 | 2,9 | 3,6 | **~2** nas cenas das duas | 1,0–1,5 |
| Pausa antes da fala (mediana) | **0,56 s** | 0,68 s | 0,82 s | 0,60 s | **1,5–2 s** | 1,3–2,9 s |
| Variação de tom (mediana) | 5,9 st | 6,9 st | 5,2 st | 6,8 st | — | — |

**As falas emocionais de Olivia são as mais rápidas e as mais chapadas do episódio:**

| Fala | Cena | Palavras/s | Variação de tom |
|---|---|---|---|
| "Around the time I left." | SC007 | **6,6** | **2,4 st** |
| "I thought it would be easier." | SC004 | 5,6 | 3,6 st |
| "I told her the truth." | SC008 | 5,2 | 3,2 st |
| "What happens to the things people leave behind?" | SC003 | 4,3 | 3,2 st |
| "Which part?" | SC003 | 5,0 | 1,9 st |
| "Your rule." | SC007 | 4,3 | 4,8 st |

Para comparar: a fala de Claire **"You don't get to decide that for me."** tem 14,3 st e vem depois de 5 s de silêncio. É o único momento do episódio em que o ritmo e a voz respiram, e é o que funciona.

**O episódio tem 8:22; o animatic tinha 10:43.** Saíram **2:20 de silêncios e planos de reação**. As falas foram coladas umas nas outras, como no piloto.

## 2. O que a imagem mostra (quadros das falas-chave)
- **Boca aberta no meio da fala** em quase todos os planos de Olivia: o rosto "falando", nunca o rosto "sentindo". É o problema que a regra E9 previa: keyframe ou geração neutra vira vídeo neutro.
- **"That's very reasonable."** (SC001): Olivia **rindo aberto**, de olhos fechados. A direção era *"amusement softening into something warmer"*.
- **SC007 e SC008:** o rosto é o mesmo em "I photographed…", "Around the time I left", "Your rule", "She asked…" e "I told her the truth": a mesma expressão neutra, a boca meio aberta, o olhar sem direção.
- **"About that."** (SC008) é o único plano com emoção no rosto (de perfil, para a janela), e é justamente o plano **sem fala na imagem**.

## 3. As causas (pelo que dá para medir)
1. **A montagem tirou os silêncios.** Com pausas de 0,6 s, nenhuma interpretação parece emocionada. Isso vale para as quatro personagens, mas pesa mais em Olivia.
2. **Olivia fala rápido demais em cada geração.** 4,5 palavras/s é ritmo de conversa apressada. O pedido "two words per second" não está sendo seguido pelo H3 nas falas dela, e falas curtas geradas em clipes curtos saem atropeladas.
3. **Olivia não tem referência de voz.** Claire e Maya têm (`@VOZ_`). A voz de Olivia sai do H3 sem referência e é convertida depois. **A conversão troca o timbre, mas mantém a entonação** da origem, que já veio chapada.
4. **O rosto falando apaga a emoção.** Nos planos em que ela fala, o H3 privilegia a boca; a emoção aparece nos planos sem fala.

## 4. Proposta de correção

### A. Remontar o EP02, sem gerar nada novo (o mais rápido)
- Voltar às pausas do pacote: **1,5–2 s** entre as falas de Claire e Olivia, até 3 s nos picos. Deixar o episódio voltar para perto de **10:00–10:40**.
- **Usar os planos de reação** (o rosto de quem escuta, com a fala da outra por cima), que estão nos pacotes do H3 e somem do corte.
- Nos picos, **cobrir a fala de Olivia com o plano dela sem fala** (o rosto emocionado) e deixar só a voz.
- **Desacelerar as falas de Olivia em 10–15%** na edição, onde não distorcer.

### B. Regerar as falas-chave de Olivia (o que resolve a voz)
1. **Criar `@VOZ_OLIVIA`:** uma referência de voz de 5–7 s, como fizemos com Claire e Maya. Candidata no próprio EP02: **"I didn't want the first time I saw you to be across a conference table."** (3:14), que é a fala de Olivia com mais variação de tom (14,3 st) e o ritmo mais lento. Eu recorto e você aprova ouvindo.
2. **Regerar só as falas-chave** (lista abaixo), com `@VOZ_OLIVIA` e:
   - **clipe longo para fala curta** (6–8 s para "Around the time I left."), para o modelo não atropelar;
   - **a pausa escrita dentro da fala**: *"Around the time... [pause] ...I left."*;
   - **3 tentativas por fala**, e a escolhida é a que eu medir mais lenta e com mais variação;
   - o rosto: **os olhos antes da boca**. O bloco pede *"her eyes fill before she speaks; her mouth barely opens"*.
3. **Falas para regerar (10):**
   - SC001: "That's very reasonable."
   - SC003: "What happens to the things people leave behind?"
   - SC004: "Yes." · "I didn't want the first time…" · "I thought it would be easier."
   - SC007: "I photographed this street once. A long time ago." · "Around the time I left." · "Your rule."
   - SC008: "She asked if I knew it was her project." · "I told her the truth."

### C. Para o EP03 em diante (prevenção)
- **`@VOZ_OLIVIA` em todos os pacotes**, como Claire e Maya (método A).
- **Duração do clipe por fala** escrita no pacote (falas curtas em clipes longos).
- **Checagem antes da entrega:** o videomaker me manda cada cena montada, eu meço (palavras/s, pausas, variação de tom) e só então a cena é dada como final. É a regra E11, que precisa virar etapa obrigatória.

## 5. Para decisão
1. Qual caminho para o EP02: **A** (remontar), **B** (regerar as 10 falas com `@VOZ_OLIVIA`) ou **A + B** (recomendado).
2. Criar **`@VOZ_OLIVIA`** a partir da fala de 3:14 (eu recorto e mando para você ouvir).
3. A **checagem medida antes da entrega** como etapa obrigatória para todos os episódios.
