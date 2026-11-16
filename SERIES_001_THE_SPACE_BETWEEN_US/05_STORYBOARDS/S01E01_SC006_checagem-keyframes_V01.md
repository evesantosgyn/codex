# Checagem de keyframes — S01E01 · SC006 "Professional Boundaries" · V01

**Data:** 2026-11-16 · **Base:** decupagem V01 (APROVADA), pacote ChatGPT SC006, V42, `continuidade.yaml`
**Recebido:** `S01E01_SC006_KEYFRAMES_APROVADOS.zip` (10 imagens, 1670×941, 16:9)
**Nota da produção:** os slides já vêm **escritos nas telas por escolha da produção**. Isso substitui o "slides compostos na pós" da V42 (proposta **V43**, abaixo).

## Resultado por imagem
| Keyframe | Rosto | Cabelo | Figurino | Relógio | Cenário / luz | Tela | Veredito |
|---|---|---|---|---|---|---|---|
| PLATE-ROOM V01 | — | — | — | — | ✔ vidro, maquete no centro, tela no fundo, nublado | branca | ✔ |
| C1 V01 | ✔ | ✔ franja, castanho-escuro | ✔ L5, batom vinho, colar duplo | ✔ pulso esquerdo | ✔ | **branca** (ver item 5) | ✔ |
| C2 V01 | ✔ | ✔ | ✔ | — | ✔ | — | ⚠️ **olhar para o lado errado** (item 2) |
| OTS-SCREEN V02 | ✔ (de costas) | ✔ | ✔ | — | ✔ | ✔ "DOCUMENTARY PRODUCTION / OLIVIA HAYES / JUNE PARK", grafia certa | ✔ para SH16 · ✖ para SH04 (item 3) |
| INS-REMOTE V01 | — | — | ✔ seda preta, anéis | ✔ | ✔ | slide de Olivia ao fundo | ✔ para SH24 · ✖ para SH03 (item 4) |
| INS-SCREEN V01 | — | — | — | — | — | **é um laptop**, com slide de capa | ✖ (item 1) |
| M1 V03 | ✔ olhos verdes, sardas | ✔ cachos no queixo | ✔ preto | — | ✔ | — | ✔ |
| M2 V01 | ✔ | ✔ | ✔ | — | ✔ | — | ✔ meio sorriso |
| TEAM V01 | — | — | **figurantes diferentes da V42** | — | ✔ | — | ⚠️ (item 6) |
| WS V03 | ✔ | ✔ | ✔ | ✖ **pulso direito** | ✔ | slide de capa **com texto em português** | ✖ (item 7) |

## Problemas e recomendações
1. **INS-SCREEN V01 é a tela de um laptop**, não a tela da parede, e mostra a capa, não o slide de Olivia. O SH11 é a revelação.
   → **Já resolvido sem gerar de novo:** recortei a tela do OTS-SCREEN V02 → `S01E01_SC006_KF-INS-SCREEN_V02.png` (a tela de frente com "OLIVIA HAYES / JUNE PARK", legível). O V01 fica descartado.
2. **C2: Claire olha para a DIREITA do quadro.** No C1 a tela está à esquerda dela no quadro, e a Maya (M1, M2) também olha para a direita. Os olhares não se cruzam: nem para a tela (SH12) nem no diálogo com Maya.
   → **Editar o C2 no ChatGPT** ("Editar", mesma imagem): *"Same image, same lighting and background. Only change her gaze and head turn: she looks toward the LEFT side of the frame."*
3. **SH04 precisa do slide da foto antiga do prédio**, mas o OTS-SCREEN só existe com o slide de Olivia. Usar esse no SH04 entrega a revelação antes da hora.
   → **Editar o OTS-SCREEN V02** no ChatGPT: *"Same image. Replace the slide on the screen with an old black-and-white archival photograph of a brick industrial building from the 1920s, no text."* → `KF-OTS-SCREEN-OLD`.
4. **INS-REMOTE mostra "OLIVIA HAYES / JUNE PARK" ao fundo.** Serve para o SH24 (clique que sai desse slide). No SH03 (primeiro clique) entregaria a revelação. Testei um recorte, mas ele corta o controle.
   → **Tirar o SH03**: o clique entra como som no fim do SH02 (−2 s). Menor detalhe: o controle está na mão esquerda (no C1, na direita). Num insert de 2 s, aceitável.
5. **C1 tem a tela branca** na borda esquerda, e é o plano mais usado (SH02, 17, 20, 21, 25, 27), cada vez com um slide diferente.
   → Como a câmera de Claire é **parada** (P-15), a tela é um retângulo fixo: **trocar o conteúdo na pós é simples** (capa no SH02, slide de Olivia no SH17–21, planta no SH25–27). Para isso faltam **dois slides planos** (imagem só do slide, sem sala), no mesmo estilo da capa: `SLIDE-OLD` (foto antiga do prédio) e `SLIDE-PLAN` (planta detalhada).
6. **TEAM:** saíram um **homem de uns 30 com suéter escuro e óculos** e uma **mulher de uns 30 de blazer bege, cabelo preso**, não o homem de 50 de terno cinza e a mulher de 40 de cardigã e óculos da V42. Os dois são **os mesmos no TEAM e no WS** (coerentes entre si) e não falam.
   → **Recomendo aceitar** e atualizar a descrição dos figurantes.
7. **WS V03:** (a) **Claire está à ESQUERDA da tela** (no C1 e no OTS ela está à direita): o corte do SH01 para o SH02 inverte a geografia. (b) **Relógio no pulso direito.** (c) Slide com **"PROPOSTA DE REQUALIFICAÇÃO URBANA" em português**, numa empresa de Manhattan.
   → **Gerar o WS V04**: Claire **à direita da tela** com o controle, relógio no pulso esquerdo, Maya na ponta da mesa mais próxima da câmera, o slide de capa em inglês.
8. **Capa "THE SPACE BETWEEN US":** o projeto de Claire leva o título da série. Pode ser uma piscadela intencional; se não for, use um nome de projeto. **Decisão sua.** Em qualquer caso, o subtítulo em inglês: **"ADAPTIVE REUSE PROPOSAL"**.

## Para aprovação
1. **V43:** os slides são gerados **na imagem** (escolha da produção); no C1 (câmera parada), o slide é trocado na pós.
2. INS-SCREEN V02 (recorte) no lugar do V01.
3. Correções no ChatGPT: **C2** (olhar), **OTS-SCREEN-OLD**, **WS V04**, **SLIDE-OLD** e **SLIDE-PLAN**.
4. SH03 sai (clique como som); a decupagem fica com 26 planos, ~1:31.
5. Figurantes novos aceitos.
6. Subtítulo da capa em inglês; título do projeto: manter "The Space Between Us" ou trocar.
