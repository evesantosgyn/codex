# Mapa das 15 bíblias do HPS 1.0 → arquivos do estúdio · V01

> **Status:** ✅ adotado com o HPS (P-19, 2026-11-25). Para cada bíblia do manual (`06_HPS-1.0_biblias-oficiais.md`), este mapa diz **onde a informação já está hoje** e **o que falta**.
> **Regras:**
> - o cânone existente prevalece até revisão formal;
> - nada é renomeado nem movido sem aprovação;
> - as lacunas são preenchidas **aos poucos**, quando a produção precisar delas, sem parar o EP03 (P-17).

| # | Bíblia | Responsável | Onde está hoje (TSBU) | Lacunas | Prioridade |
|---|---|---|---|---|---|
| 01 | Studio Bible | Ambos; Pedro nos padrões técnicos | `CLAUDE.md` · `00_ESTUDIO/01_manual-mestre.md`, `02_biblia-criativa.md`, `03_manual-producao-ia.md` (§12–§14), `05_HPS-1.0_padrao-producao.md` · `templates/` | Logotipo e tagline do estúdio ("Her stories. Our cinema."); custo por segundo aprovado; inventário de ferramentas e licenças (com o Pedro) | Média |
| 02 | Series Bible | Evelin | `01_SERIES_BIBLE/biblia-serie.md` · `canone-segredo-olivia.md` · `registro-decisoes.md` | Classificação pretendida; separar "canônico" de "em desenvolvimento" num índice | Baixa |
| 03 | Character Bible | Evelin | **Claire: `claire-bennett_character-bible_V01.md` (V93) + fonte canônica JSON `TSBU_CHR-CLAIRE_V01.json` com 54 expressões (V94–V104); Olivia: `olivia-hayes_character-bible_V01.md` + `TSBU_CHR-OLIVIA_V01.json`, 50 expressões (V105)** · `02_CHARACTERS/*/ficha.md` + identity pack + refs · `continuidade.yaml → fixos` · "Assinatura de cena" (E14, V82) | **Mapa de interpretação** por emoção (amor, tristeza, raiva, medo, ansiedade, alegria, ciúme, vulnerabilidade); vistas de perfil e 3/4 aprovadas | **Alta** (é o que falta para a emoção, V90) |
| 04 | Relationship Bible | Evelin | Espalhada: V70, V71, `canone-segredo-olivia.md`, escaletas | **Não existe como documento.** Fichas Claire–Olivia, Claire–Maya, Olivia–June, Maya–June: o que cada uma sabe, esconde e deseja | **Alta** |
| 05 | Location Bible | Evelin; Pedro valida | `03_LOCATIONS/*/ficha.md` + pranchas e refs | Room tone e acústica por cenário; ângulos oficiais de câmera e eixo; versões dia/noite | Média |
| 06 | Wardrobe Bible | Evelin | `continuidade.yaml` (looks por episódio) · `S01E0x_LOOK_*.png` | Look **por dia narrativo** com ID (hoje é por episódio); vista traseira e lateral | Média |
| 07 | Voice Bible | Evelin define; Pedro implementa | `continuidade.yaml → voz` · `06_GENERATED_ASSETS/VOICES/` (Claire e Maya v02) · V28, V31, V38 | **Olivia** (candidata `@VOZ_OLIVIA` aguardando aprovação) e **June** sem referência; origem e autorização das referências; motor de voz (P-17) | **Alta** |
| 08 | Cinematography Bible | Evelin + Pedro | P-15 · `03_manual-producao-ia.md` §14 · `07_EDITING/S01E03_referencia-angulos-som_V01.md` | Câmera e lentes de referência (Alexa 35, Venice 2; 24–35/50/85 mm); moodboards por ambiente; o que preservar na adaptação por motor | Média |
| 09 | Keyframe Bible | Evelin | `00_ESTUDIO/briefing-chatgpt-keyframes.md` · `templates/pacote-cena-chatgpt.md` · `chatgpt-projeto_biblia-visual.md` | **Manifesto de imagem** (ferramenta, prompt, refs, SHA-256, aprovador) por keyframe, a começar pela SC005 | **Alta** (novo a partir da SC005) |
| 10 | Color Bible | Pedro; Evelin valida | Notas de cor nos pacotes (Claire fria, Olivia quente; escurecer cabelo de Claire) | Looks por horário, espaço de cor, LUTs/PowerGrades | Pedro |
| 11 | Sound Bible | Pedro; Evelin valida | §14 E15 · notas de som dos pacotes | Biblioteca com licenças (Suno, ElevenLabs, CapCut); leitmotivs; room tones | Pedro |
| 12 | Season Bible | Evelin | `biblia-serie.md` (temporada) · escaletas e conceitos por episódio | Ficha de episódio com status (planejado → publicado) para EP01–EP03 | Média |
| 13 | Continuity Bible | Evelin lidera; Pedro registra | `continuidade.yaml` · `pendencias.md` · checklists QC | Controle por plano (agora nos cards JSON); atualizar ao fim de cada episódio a partir do **master** (o que efetivamente apareceu) | Média |
| 14 | Technical Production Bible | Pedro | `00_ESTUDIO/04_manual-ferramentas.md` (H3/LoRA, P-06–P-13, suspensos) | Tudo do lado do Pedro: ComfyUI, RunPod, LTX, SeedVR2, licenças | Pedro |
| 15 | Entrega e aprovação | Evelin + Pedro | Documentos do videomaker (Claude Docs) · pacotes · ZIPs | Gates **G1–G4** nos pacotes de cena (a partir da SC005); Episode Production Book do EP03 | **Alta** |

## Gates (G1–G4)
- **G1:** roteiro, decupagem, keyframes e animatic aprovados pela direção criativa (Evelin).
- **G2:** identidade, atuação, movimento, diálogo e continuidade validados.
- **G3:** edição, restauração, cor e som aprovados.
- **G4:** licenças, master e publicação, com aprovação conjunta.

## Próximos documentos sugeridos (do lado da Evelin, quando houver espaço)
1. **Relationship Bible** da TSBU (fichas das quatro relações).
2. **Mapa de interpretação** nas fichas de Claire, Olivia, Maya e June.
3. **Voice Bible**: aprovar `@VOZ_OLIVIA` e definir June.
4. **Episode Production Book** do EP03.
