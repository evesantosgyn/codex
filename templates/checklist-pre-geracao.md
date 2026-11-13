# Checklist pré-geração — por cena

> Obrigatório antes de gerar qualquer plano de uma cena nova. Nasceu das lições do teste da SC001 de *The Space Between Us* (ver `00_ESTUDIO/03_manual-producao-ia.md` §12). Vale para todas as séries.

Cena: ______ · Decupagem: ______ · Data: ______

## 1. Herança das cenas já aprovadas
- ☐ Assisti/conferi a **última cena aprovada** em que cada personagem e cada locação aparecem. **O material aprovado prevalece sobre planta ou prancha** quando os dois divergirem.
- ☐ Geografia da locação (posição de móveis, portas, janelas, elevador) igual à do material aprovado.
- ☐ Lado do eixo (quem fica à esquerda e à direita do quadro) coerente com a última cena no mesmo espaço, ou a mudança está motivada e indicada.

## 2. Transição entre cenas (saída → entrada)
- ☐ O que cada personagem **veste e carrega ao sair** da cena anterior é o que ela tem ao entrar nesta (casaco, bolsa, celular, pasta, câmera).
- ☐ Se algo mudou (vestiu casaco, deixou a bolsa), a mudança aparece em quadro **ou** está registrada como ação fora de quadro em `continuidade.yaml`.
- ☐ Clima e período do dia batem com a cronologia (chuva, luz, céu).

## 3. Identidade (por plano)
- ☐ Referências de identidade carregadas: LoRA da personagem + Identity Pack frontal e 3/4 + quadro do plano anterior.
- ☐ **Planos abertos, de corpo inteiro e de caminhada** (maior risco de deriva): referência de rosto **e** de cabelo; cor do cabelo descrita no texto do prompt.
- ☐ Marcas fixas (pinta, tatuagem, franja) com o **lado** correto.

## 4. Luz entre plano e contraplano
- ☐ Um **plate de locação por eixo**, gerado com o mesmo estado de céu e hora do dia.
- ☐ Plano e contraplano conferidos lado a lado **antes** da geração em série: o mesmo instante tem que parecer o mesmo instante nos dois lados.

## 5. Objetos e escala
- ☐ A escala visual dos objetos bate com o que o diálogo afirma (tamanho, quantidade, distância).
- ☐ Objeto novo que surgir numa geração aprovada (ex.: uma bolsa) é registrado **na hora** em `continuidade.yaml`.

## 6. Voz
- ☐ Clipe de referência de voz de cada personagem que fala (Voice Identity Pack) carregado na geração.
- ☐ Personagem sem voz definida: gerar e aprovar a voz **antes** da cena inteira.

## 7. Start & end frame (L9)
- ☐ Imagem inicial e final **compatíveis**: mesmo lado, mesmo eixo, objetos nas mesmas posições (só muda a distância). Se não forem, dividir em dois planos com corte.

## 8. Técnico
- ☐ Duração pedida ≥ mínimo da ferramenta (no H3, 4–5 s); o corte fino fica para a montagem.
- ☐ Resolução e proporção de saída anotadas (o master final é **3840 × 2160**, 16:9).
