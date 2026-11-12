---
name: checagem-continuidade
description: Verifica a continuidade de personagens, locações, figurino, objetos e cronologia contra o registro canônico da série. Use quando receber novas pranchas, keyframes, frames gerados, roteiros ou fichas, ou quando pedirem para checar consistência ou continuidade.
---

# Checagem de continuidade

## Fontes canônicas
`continuidade.yaml` (traços fixos, looks, cronologia) · fichas em `02_CHARACTERS/` e `03_LOCATIONS/` · pranchas `.webp` · `registro-decisoes.md` · `pendencias.md`.

## Para material visual (pranchas, keyframes, frames)
Abra cada imagem e compare com a prancha canônica e o YAML:
1. **Rosto:** estrutura facial, formato dos olhos, sobrancelhas, boca, mandíbula.
2. **Traços fixos:** cor dos olhos e do cabelo, comprimento e corte, marcas (pinta, tatuagem, sardas), com o lado correto.
3. **Mãos:** anatomia, anéis, relógio no pulso correto.
4. **Figurino:** o look corresponde ao designado para a cena?
5. **Acessórios assinatura** presentes e consistentes.
6. **Locação:** móveis, objetos fixos, posição das janelas e portas segundo a planta oficial; luz conforme o padrão do período.
7. **Semelhança com pessoa real:** se um rosto parecer reproduzir alguém real identificável, sinalize (não nomeie a pessoa; descreva o risco).

## Para texto (roteiros, fichas, escaletas)
- Idades, profissões, relações e nomes batem com o YAML e as fichas?
- A cronologia (dias da semana, períodos, "tomorrow", "Monday") é coerente?
- Eventos já revelados e pontas abertas são respeitados (nada revelado cedo demais pelo cânone V2.2)?
- Conteúdo travado preservado literalmente?

## Saída
Relatório com três seções:
1. **Conforme:** o que bate.
2. **Divergências:** tabela item | fonte A | fonte B | gravidade (alta/média/baixa) | impacto nas cenas.
3. **Recomendações:** solução sugerida para cada divergência.

Adicione cada divergência nova em `pendencias.md` com o próximo número livre (Pxx). **Nunca altere o cânone para "resolver" uma divergência sem decisão do responsável.**
