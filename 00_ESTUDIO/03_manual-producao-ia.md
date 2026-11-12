# Manual de Produção Cinematográfica com IA

Documento Mestre 02 (v1.0) + Documento Mestre 03 (pipeline técnico) · Fonte: `fontes/ficha-tecnica-completa.pdf`

O ponto central: **um processo repetível e controlável, para que a qualidade não dependa da sorte de uma geração de vídeo.**

Prioridade de qualidade cinematográfica máxima em três aspectos: **consistência das protagonistas, interpretação emocional e naturalidade das cenas.**

**Ordem recomendada:** prova de conceito cinematográfica → episódio piloto completo → temporada, somente após validação.

## 1. Arquitetura de produção
| Fase | Nome | Entrega |
|---|---|---|
| 01 | SCRIPT LOCK | Roteiro aprovado e cenas numeradas |
| 02 | VISUAL DEVELOPMENT | Elenco virtual, cenários e identidade visual |
| 03 | SHOT DESIGN | Storyboard e decupagem cinematográfica |
| 04 | AI GENERATION | Produção de planos e performances |
| 05 | AUDIO & EDITING | Vozes, trilha, montagem e finalização |
| 06 | QUALITY CONTROL | Revisão e aprovação do episódio |
| 07 | MASTER & DELIVERY | Exportação, legendas e publicação |

Cada fase tem entregáveis e critérios de aprovação. Um roteiro aprovado não é modificado silenciosamente durante a geração; alterações narrativas são registradas.

**Regra central:** não gerar o vídeo inteiro de uma vez. Primeiro aprovamos personagens e keyframes; depois produzimos planos controlados, montamos as performances e finalizamos o episódio. Assim dá para corrigir uma tomada sem reconstruir a cena toda.

## 2. Elenco virtual
Uma protagonista não pode parecer uma mulher diferente a cada episódio: identidade visual **reproduzível**, não só descrição textual.

**Character Identity Pack** (por personagem principal): retrato frontal, três quartos, perfis, corpo inteiro, expressões, figurinos, voz de referência e características que não podem mudar.

**Regras de consistência:**
1. Usar imagens canônicas aprovadas como referência de geração, quando a ferramenta permitir.
2. Preservar estrutura facial, proporções, marcas distintivas e identidade vocal.
3. Diferenciar características permanentes de mudanças temporárias de figurino e aparência.
4. Verificar rosto, mãos, cabelo, acessórios e proporções em cada plano.
5. Rejeitar e regenerar tomadas em que a identidade da personagem se perca.

A continuidade é verificada visualmente: nenhum prompt garante identidade perfeita sozinho.

## 3. Direção de fotografia e linguagem
Pensar como diretor de cinema, não como quem só escreve prompts. Cada cena tem intenção dramática e estratégia visual correspondente.

| Plano | Uso |
|---|---|
| Establishing / Wide | Apresenta o espaço, a relação entre personagens e o contexto emocional; inicia cenas e estabelece geografia |
| Medium / Two-Shot | Linguagem corporal, distância física e dinâmica; fundamental para diálogos |
| Close-Up | Microexpressões, hesitações e emoções; quando o rosto conta mais que as palavras |
| Over-the-Shoulder / Reverse | Relação espacial; constrói diálogos pela montagem |

**Regra de direção:** nenhum movimento de câmera só para impressionar. Uma aproximação revela mudança emocional, descoberta ou intimidade. Câmera estática pode ser mais poderosa que um travelling quando o silêncio é o centro.

## 4. Decupagem para geração de vídeo
- Estratégia inicial: **image-to-video com referências controladas**, complementada por text-to-video quando adequado.
- Sempre que possível, aprovar primeiro a composição visual do plano (keyframe) e usá-la para orientar a animação.
- **Ficha técnica por plano:** identificador, duração pretendida, personagens presentes, imagem inicial, movimento, ação, emoção, áudio e ligação com o plano seguinte (`templates/ficha-plano.md`).
- Preferir tomadas curtas e controláveis quando a cena for complexa. A duração de cada geração segue as capacidades da ferramenta escolhida, não uma regra fixa do agente.

## 5. Diálogos, atuação e vozes em inglês
Três tarefas separadas:
1. **Escrita dramática:** inglês natural, com vocabulário, ritmo e personalidade diferentes entre as personagens.
2. **Direção de interpretação:** intenção, pausas, respiração, hesitações, intensidade e emoção de cada fala.
3. **Realização audiovisual:** geração de voz, sincronização labial, expressão facial e montagem.

Evitar que todas falem igual (uma executiva britânica de 42 anos não fala como uma fotógrafa americana de 27).

**Roteiro de performance (exemplo do manual):**
```
SCENE 014 — INT. APARTMENT — NIGHT
EMMA (quietly, avoiding eye contact)
"You could've told me."
SOPHIA (a long pause; barely above a whisper)
"I know."
Emma looks toward the door. Sophia takes a small step forward, then stops.
EMMA
"Then why didn't you?"
```
Objetivo: atuação com intenção e subtexto. Lip-sync tecnicamente correto não basta.

**Voice Identity Pack:** timbre, sotaque, cadência, intensidade e amostras autorizadas. **Sem clonagem de voz de pessoas reais sem permissão.**

## 6. Áudio e desenho sonoro
Quatro camadas independentes: **diálogos, ambiência, efeitos sonoros, música.** A trilha não preenche automaticamente todos os silêncios; em cenas de intimidade, o som ambiente, a respiração e a ausência de música podem ter mais força. O agente prepara orientações de mixagem e verifica se as licenças de músicas, vozes e efeitos permitem publicação e monetização.

## 7. Ferramentas (candidatas — NÃO validadas)
| Departamento | Candidatas | Função |
|---|---|---|
| Roteiro e direção | (agente showrunner) | Showrunner, bíblias e decupagem |
| Imagens e referências | ChatGPT Images, Midjourney | Personagens, cenários e keyframes |
| Produção | **ComfyUI** (aprovado; workflows dependem dos modelos instalados) | Pipeline de geração |
| Vídeo | Runway, Kling, Google Veo | Animação e geração de tomadas |
| Vozes | ElevenLabs | Interpretação e identidade vocal |
| Música | Suno | Trilhas originais, conforme licenciamento |
| Montagem | DaVinci Resolve, Premiere Pro | Edição e finalização |
| Legendas | Whisper + ferramentas de edição | Transcrição, tradução e sincronização |

Antes do pipeline definitivo, comparar resultados, preços, limites de geração, consistência de personagens, lip-sync e direitos comerciais. O estúdio não pode depender de uma única plataforma.

**Arquitetura técnica recomendada:** Showrunner (roteiro, direção e supervisão) → Elenco e cenários (imagens canônicas) → Geração de vídeo (modelo principal + alternativo) → Voz e performance (vozes consistentes, lip-sync) → Montagem (DaVinci/Premiere) → Controle de qualidade (revisão visual, narrativa e técnica) → Distribuição (YouTube, redes, assinaturas).

## 8. Padrão de prompts
Em **inglês**, mesmo com a discussão em português. Campos claros, sem instruções vagas ou contraditórias. Modelo em `templates/prompt-plano.md`. Os campos são adaptados à sintaxe e aos recursos da ferramenta escolhida; nunca um prompt genérico idêntico para todos os modelos.

## 9. Controle de qualidade do episódio
Checklist obrigatório antes de qualquer publicação: `templates/checklist-qc.md`.

## 10. Organização dos arquivos
```
STUDIO_GL_AI/
  SERIES_001/
    01_SERIES_BIBLE/
    02_CHARACTERS/{CHARACTER_A,CHARACTER_B,...}/
    03_LOCATIONS/
    04_SCRIPTS/
    05_STORYBOARDS/
    06_GENERATED_ASSETS/{IMAGES,VIDEO,VOICES,MUSIC}/
    07_EDITING/
    08_FINAL_MASTERS/
    09_SUBTITLES/
    10_MARKETING/
    11_PERFORMANCE_REPORTS/
```
Identificadores únicos: `S01E02_SC014_SH03_V02` = segunda versão da terceira tomada da cena 14, segundo episódio, primeira temporada. Assim dá para substituir uma tomada sem comprometer o resto da montagem.

## 11. Entrega de um episódio
Pacote completo: (1) roteiro aprovado em inglês · (2) escaleta e mapa de ritmo · (3) lista de cenas e tomadas · (4) referências de personagens, cenários e figurinos · (5) prompts por geração · (6) orientações de voz, interpretação e som · (7) plano de montagem e transições · (8) checklist de continuidade e qualidade · (9) materiais de lançamento e distribuição.

**Limite operacional:** o agente planeja, cria materiais e orienta a produção. Geração, edição e publicação efetivas dependem das ferramentas e integrações disponíveis. Não confundir plano de produção com episódio finalizado.

## 12. Lições aprendidas — regras de produção

Aprovadas pelo responsável em 2026-11-12, a partir do teste da SC001 de *The Space Between Us*. Valem para **todas as cenas seguintes e todas as séries**. O checklist operacional está em `templates/checklist-pre-geracao.md`.

| # | O que aconteceu | Regra a partir de agora |
|---|---|---|
| L1 | O cabelo da protagonista **mudou de cor** nos planos de caminhada e corpo inteiro | Planos abertos e de caminhada levam referência de rosto **e** de cabelo, mais o quadro do plano anterior; a cor do cabelo é conferida plano a plano antes da aprovação |
| L2 | Plano e contraplano do **mesmo instante** saíram com luz diferente (noite × pôr do sol) | Um plate de locação por eixo, com o mesmo céu; plano e contraplano conferidos lado a lado antes da geração em série |
| L3 | A personagem saiu de uma cena **sem o casaco** que precisa ter ao entrar na seguinte | Checar o que cada personagem veste e carrega na **saída** de uma cena e na **entrada** da próxima |
| L4 | O diálogo diz "quatro milímetros" e o objeto em quadro tem ~2 cm | A escala visual dos objetos precisa bater com o que o diálogo afirma; se não bater, aceitar conscientemente (a piada sobrevive?) |
| L5 | A geração inventou um objeto bom (bolsa) que não estava na continuidade | Objeto novo em take aprovado entra no `continuidade.yaml` na hora e passa a ser obrigatório nas cenas seguintes |
| L6 | O material aprovado ficou com geografia e eixo diferentes da planta e da decupagem | **Material aprovado prevalece** sobre planta, prancha e decupagem. As fichas são atualizadas para o "as built" |
| L7 | Saída 3868 × 2160 e áudio a −32 dB de média | Master final em **3840 × 2160**; normalizar o áudio na mixagem (meta de loudness a definir com a plataforma) |
| L8 | Dedos manipulando objeto pequeno funcionaram bem no H3 | Não complicar a encenação por medo de anatomia: testar primeiro e só então recorrer a inserts ou ferramentas |
