# Pendências e contradições abertas

O agente **não resolve estes itens sozinho**. Cada um precisa de decisão do responsável e, depois, de registro em `registro-decisoes.md`. Quando um item for resolvido, mova-o para a seção "Resolvidas" com a decisão e a data. Novas pendências usam o próximo número livre (**P24**).

## Abertas

### P11 — Pipeline técnico (PARCIAL)
- ✅ Vídeo: **MiniMax H3 (Hailuo 3)**. ✅ Consistência: **LoRA** por personagem (decisão de 2026-11-12; ver `00_ESTUDIO/04_manual-ferramentas.md`).
- Falta: modelo-base das LoRAs e onde rodam; quais personagens já têm LoRA; ferramenta de imagem/keyframe; origem das vozes ✅ (áudio nativo do H3); montagem; legendas; workflows do ComfyUI; se o 3868×2160 do teste veio de upscale.
- Frameworks e prompts de execução existentes: **aguardando envio**.

### P12 — Materiais e referências ainda não recebidos
- ~~Os 18 keyframes travados da Cena 003~~: **dispensados** (N18: a produção da SC003 será refeita). Pinta, tatuagem e casaco da Olivia **definidos** (V26, V27).
- Prancha atualizada do escritório com as áreas da Planta A sobre a Planta B (opcional; a ficha já descreve em texto).
- Sala de conferência da SC006 (pode ser a sala de reuniões de vidro da planta oficial).
- Equipe de redevelopment da SC006: 2 figurantes sem referência visual.
- Voice Identity Packs: ferramenta definida (**áudio nativo do MiniMax H3**). ✅ Clipes de referência de **Claire** e **Maya** extraídos da SC001 (2026-11-12); ampliados na v02 (Claire 5,6 s; Maya 6,85 s). Falta definir as vozes de **Olivia** (SC003) e **June** (SC005).

## Resolvidas

### P23 — EP02 aprovado × limites das Character Bibles (2026-11-28)
O EP02 foi decupado e gerado antes das bíblias (V93–V127). Ao refazer as decupagens cinematográficas do EP02, três planos aprovados contrariam limites aprovados depois:
- **(a) Olivia, SC004 SH24:** o pacote do EP02 (V70) pede **uma lágrima que cai** no rosto de Olivia. A bíblia dela (V105) diz: **lágrima caindo só a partir do EP05** (EXP-O-33).
- **(b) Claire, SC009 SH20:** o pacote pede, no escuro, **uma lágrima que escorre e ela enxuga** (nível 2). A bíblia de Claire diz: **nível 2 só na SC006 do EP03** (EXP-C-26).
- **(c) Claire, SC009 SH09 (KF-BROLL):** Claire **ri de verdade, de cabeça para trás**, no plano de cobertura gravado naquela manhã. A bíblia diz: **riso aberto nunca na T1**.
- **Decidir, item a item:** manter o EP02 como está e registrar o plano como exceção aprovada na bíblia, **ou** ajustar na remontagem (correção A). Opções possíveis: em (a), cortar antes da lágrima cair (O-29); em (b), ir ao preto antes da lágrima (C-25); em (c), não há corte possível sem perder o gancho, e a exceção precisaria ser registrada.
- **Recomendação do Showrunner:** (a) e (b), cortar antes da lágrima na remontagem, o que preserva a primeira lágrima de Olivia para o EP05 e a única de Claire para a SC006 do EP03; (c), registrar como exceção, porque é imagem gravada e é o gancho do episódio.
- ✅ **Resolvida (2026-11-28, V134):** as três recomendações: (a) e (b) cortadas na remontagem antes da lágrima; (c) exceção registrada na bíblia de Claire

### P20 — HPS 1.0: H3 suspenso × pipeline aprovado no H3 (2026-11-25)
- O **HPS 1.0** (`00_ESTUDIO/05_HPS-1.0_padrao-producao.md`) diz: **"H3 suspenso até esclarecimento de licença"**; LTX em validação; o pacote de cena **nunca depende de um só modelo** (prompt neutro + adaptador por motor).
- Decisões aprovadas que dependem do H3: **P-06** (vídeo no H3), **P-07** e **P-13** (vozes nativas do H3 com `@VOZ_`), os pacotes "pacote-H3" do EP03 (CO–SC004, V84–V89) e a **correção B do EP02** (V90: regerar 10 falas de Olivia com `@VOZ_OLIVIA` no H3).
- **Decidir:** o HPS substitui essas decisões? Os pacotes do EP03 já entregues viram "adaptador H3" (válido só se a licença for liberada)? E a correção B do EP02 espera o motor definitivo?
- ✅ **Resolvida (2026-11-25, P-17):** documento criativo neutro + adaptadores do Pedro por motor; pacotes H3 do CO–SC004 preservados e convertidos quando entrarem em produção; H3 suspenso; LTX não aprovado até os benchmarks; correção B do EP02 espera o motor

### P21 — HPS 1.0: convenção de nomes de arquivo (2026-11-25)
- HPS: `TSBU_S01E03_SC001_SH01_KF_V01.png` (prefixo da série, keyframe **por plano**, e também RAW, RST, VOX, WF, MASTER).
- Hoje: `S01E03_SC004_KF-C-GAP_V01.png` (keyframe **por ID**, reaproveitado em vários planos), conforme o `CLAUDE.md`.
- O HPS manda **não mover arquivos antigos sem autorização**. **Decidir:** adotar o padrão do HPS só para arquivos novos (a partir da SC005) e como o keyframe reaproveitado é nomeado (por plano de origem ou por ID).
- ✅ **Resolvida (2026-11-25, P-18):** padrão do HPS para arquivos novos; o keyframe leva o número do primeiro plano em que aparece

### P22 — HPS 1.0: status do documento (2026-11-25)
- O documento é a **"Versão 1.0 para aprovação dos sócios"**, com as assinaturas de Evelin e Pedro em branco. A responsável o enviou como **indispensável** para os próximos passos.
- **Decidir:** o HPS está aprovado pelos dois sócios (entra no registro como decisão) ou é aplicado como proposta até a assinatura?
- ✅ **Resolvida (2026-11-25, P-16):** aprovado pelos dois sócios; adotado oficialmente a partir da SC005 do EP03

### P19 — Anéis e colar de Claire: `continuidade.yaml` × decisões do EP02/EP03
- O `continuidade.yaml` (assinatura de Claire, versão do piloto) lista **"anéis finos dourados"** e **"colar duplo dourado (pingente escuro + pingente circular)"**.
- As decisões do EP02 e do EP03 pedem **sem anéis** e **UM pingente vermelho-escuro**: V66 (o C11 refeito "sem anel e sem a segunda corrente") e V75 ("NO rings" nos keyframes do EP03). Os pacotes do EP02 e do EP03 já seguem isso.
- **Decidir:** (a) do EP02 em diante Claire usa **sem anéis e um pingente só**, e o `continuidade.yaml` é atualizado; ou (b) anéis e colar duplo continuam valendo e os pacotes mudam. A bíblia visual do Projeto do ChatGPT foi escrita com (a), marcada como pendente.
- ✅ **Resolvida (2026-11-23, V83): opção (a).** Do EP02 em diante, Claire **sem anéis** e com **um pingente vermelho-escuro só**; `continuidade.yaml` atualizado.


| # | Tema | Decisão | Data |
|---|---|---|---|
| P18 | "Blouse" no roteiro do EP02 × gola alta (V54) | A peça de cima de Claire vira **"turtleneck"** no cold open, na SC002 e na SC004; roteiro promovido a **V1.2** | 2026-11-17 |
| P01 | Idade de June Park | **34 anos**; roteiro corrigido (V3.1) | 2026-11-12 |
| P02 | Profissão de Maya | **Arquiteta sênior que gerencia os projetos do estúdio**; SC001 corrigida (V3.1) | 2026-11-12 |
| P03 | Aparência de Maya | **Prancha**: olhos verdes, cabelo ondulado na altura do queixo | 2026-11-12 |
| P04 | Plantas do escritório | **Planta B oficial** + áreas da Planta A (sala de Claire, sala de reuniões, lounge) e janelas a oeste | 2026-11-12 |
| P05 | Planta do apartamento | **Corrigida só em texto** (ver `03_LOCATIONS/APARTAMENTO_CLAIRE/ficha.md`): o "3" noroeste é a cozinha (4); o bloco central de estantes é o escritório (8). A imagem é mantida. Conferir com os keyframes da SC003 quando chegarem (P12) | 2026-11-12 |
| P06 | "You cut your hair" | **A franja é nova.** Há sete anos: cabelo longo e ondulado, sem franja | 2026-11-12 |
| P07 | Numeração de planos | **Recomeça em cada cena** (SH01…). SH29–SH34 da SC001 serão renumerados | 2026-11-12 |
| P08 | Nome do café | **"The Quiet Hour"** | 2026-11-12 |
| P09 | Semelhança com pessoas reais | Verificado pelo responsável. **Rostos de Claire e Olivia TRAVADOS** | 2026-11-12 |
| P10 | Aprovações formais | **Aprovados**: conexão profissional (N05), roteiro (N08, agora V3.2), Maya e June recorrentes (N09) | 2026-11-12 |
| P13 | Cronologia | **"It's Thursday"** na SC002: SC001–SC003 na quinta, SC004–SC009 na sexta | 2026-11-12 |
| P17 | Pulso do relógio de Claire | **Esquerdo** daqui em diante; a SC001 (direito) fica como divergência aceita | 2026-11-12 |
| P16 | Fala fora de quadro (V.O.) | Planos-fonte no H3 com referência de voz; só o áudio, com EQ de celular | 2026-11-12 |
| P14 | Olivia sabia que o estúdio era o de Claire? | **Sim.** Sabia antes de bater na porta e não contou | 2026-11-12 |
| P15 | Claire já morava no apartamento há sete anos? | **Sim.** Olivia conhece o prédio e o porteiro | 2026-11-12 |
| — | Gesto da SC004 (escaleta × roteiro) | **Entra como gesto mudo**: Claire abre o contato antigo de Olivia, hesita e bloqueia a tela | 2026-11-12 |
