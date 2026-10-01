# Dúvidas para o professor — TP1 (conceito autoral)

> Documento de trabalho, **sprint-02 em aberto**. Reúne as decisões ainda não travadas e as
> perguntas a levar ao professor antes de fechar o conceito. Nada aqui está commitado como final.

**Data:** 2026-09-10 · **Estado:** conceito candidato = SCED (ver `conceito-autoral.md`), não fechado.

---

## Resumo de onde chegamos

Concebemos, por raciocínio próprio, um método: **SCED — Seleção Convergente de Extremos Distintos**.
Em cada passada ele acha o **menor** e o **maior** valor distinto e joga **todas as cópias** de cada
um para as duas extremidades, convergindo de fora para dentro. Custo **Θ(n·d)**, d = nº de valores
distintos (melhor caso Θ(n) com poucos distintos; pior caso Θ(n²) com tudo distinto). É **in-place**
(O(1) de memória) e por comparação.

Na verificação de originalidade descobrimos que o **núcleo coincide com o Bingo Sort** (variante
conhecida do Selection Sort, catalogada no NIST). Nosso diferencial proposto é a **colocação
bidirecional convergente** (dois extremos por passada) + a análise em função de `d`.

---

## Perguntas a levar ao professor

### 1. Originalidade vs. Bingo Sort *(a mais importante)*
Nosso núcleo é o Bingo Sort. Assumindo declaração explícita da origem + a extensão bidirecional
convergente e a comparação com a literatura:
- Isso caracteriza **"adaptação estrutural profunda"** aceita (seção 2 do enunciado), ou o senhor
  consideraria **"variação cosmética"** (risco de nota 0,0)?
- Que profundidade de modificação o senhor espera para aceitar como autoral?

### 2. Atalho de "já ordenado" (melhoria A) — é legítimo?
Adicionamos uma passada inicial O(n) que detecta se o vetor já está ordenado e, se estiver, retorna
imediatamente. Isso transforma o cenário obrigatório "vetor já ordenado" em melhor caso trivial O(n).
- O senhor **quer ver** esse atalho (adaptatividade é uma virtude), ou prefere avaliar o
  **comportamento natural do núcleo** no cenário ordenado (sem atalho)?
- Um algoritmo pode "detectar e sair" no cenário de teste obrigatório, ou isso é visto como burlar o
  espírito do teste de melhor caso?

### 3. Contagem de "movimentações" — convenção esperada
O contrato é `(lista_ordenada, comparacoes, movimentacoes)`. Numa abordagem **em árvore** (ver dúvida
4) não há troca de elementos de vetor — há criação de nós/ponteiros.
- Como o senhor espera que contabilizemos "movimentações" fora de um algoritmo baseado em trocas?
- No SCED in-place, contar cada swap como 2 movimentações está de acordo com o esperado?

### 4. Caminho em árvore — conta como autoral?
Medimos uma versão em árvore (BST com contador por nó) que atinge **O(n log d)** — bem mais rápida em
comparações que o SCED (ver tabela abaixo). Mas:
- Árvore de busca + in-order **é o Tree Sort clássico**. Para sobreviver aos testes obrigatórios de
  "ordenado" e "reverso" (onde a BST desbalanceada degenera para O(n²)), seríamos **obrigados** a
  implementar uma **árvore balanceada (AVL/Rubro-Negra)**.
- Isso ainda conta como autoral (adaptação declarada de Tree Sort), ou é mais prudente **manter o
  SCED** e usar a árvore **apenas na seção de comparação com a literatura**?

### 5. Propriedades exigidas
- **Estabilidade** é exigida/valorizada? (o SCED por trocas **não** é estável.)
- **In-place (O(1))** é valorizado a ponto de justificar abrir mão de velocidade? Isso decide o
  fork SCED (O(1), Θ(n·d)) vs árvore (O(d)/O(n), O(n log d)).

### 6. Formato de entrega
Confirmar: vamos de **slides** (Opção B) + código executável. Correto?

---

## Dados empíricos que embasam as perguntas (n = 500)

### Fork central: SCED (in-place) vs Árvore (BST c/ contador)

| Cenário | d | SCED comp | Árvore BST comp | Árvore *balanceada*~ | Memória árvore |
|---|---|---|---|---|---|
| aleatório amplo | 500 | 250.999 | **4.516** | 4.482 | 500 nós |
| floats | 500 | 250.999 | **4.454** | 4.482 | 500 nós |
| aleatório estreito | 10 | 6.264 | **1.574** | 1.660 | 10 nós |
| poucos distintos | 5 | 3.647 | **1.271** | 1.160 | 5 nós |
| **já ordenado** | 500 | **1.497** | 124.750 💀 | 4.482 | 500 nós |
| **reverso** | 500 | 250.999 | 124.750 💀 | 4.482 | 500 nós |

**Insight dos "calcanhares opostos":** o SCED tem melhor caso no vetor ordenado e pior no reverso; a
BST desbalanceada é o inverso (péssima no ordenado, boa no aleatório). A árvore ganha em velocidade
média, mas custa O(d) de memória e recai sobre um clássico.

### Melhorias testadas no SCED
- **A (atalho ordenado):** `ordenado` caiu de 250.500 → **1.497** comparações (−99%). **Adotada.**
- **B (fundir busca de min/max na partição):** **não ajudou** (+0%, às vezes pior). Lição: descobrir
  min/max custa as mesmas comparações independente de onde se faça. **Descartada.**

---

## Como validamos o cenário "ordenado" (contra alucinação de teste)

Preocupação legítima: um atalho de "já ordenado" é exatamente onde um teste pode passar sem provar
nada. Fizemos verificação **independente** (oráculo = `sorted()` do Python, não o próprio algoritmo):

1. **Equivalência lógica (50.000 casos):** o critério do atalho dispara **exatamente** quando o vetor
   está ordenado — **0 divergências** contra um oráculo `is_sorted` independente.
2. **Adversarial (50.000 casos):** vetores com **1 inversão forçada** → o atalho **nunca** disparou
   (0 falsos positivos).
3. **Fuzz (40.000 casos):** SCED com e sem atalho → **0 saídas erradas** contra `sorted()`.
4. **Cross-check:** o núcleo **sem** o atalho (v2) ordena o vetor ordenado corretamente (250.500
   comparações). Logo, o atalho é otimização, não muleta para esconder bug.

> **Ressalva honesta (levar ao professor):** quando o atalho dispara, o **núcleo convergente não é
> exercitado**. Portanto, no cenário obrigatório "ordenado", a versão final só testa o atalho — por
> isso mantemos o protótipo sem atalho (v2) para validação cruzada do núcleo.

> **Meta-lição de pensamento crítico:** nosso **primeiro** script de verificação tinha um defeito —
> usava `passes == 1` como sinal de "atalho disparou", mas `passes == 1` também ocorre quando o núcleo
> resolve em uma passada (2 valores distintos). Só percebemos porque **desconfiamos do instrumento**,
> não do resultado. Isso ilustra o que as Regras do Jogo pedem: validar a própria ferramenta.

---

## Artefatos de referência
- `conceito-autoral.md` — descrição do SCED (candidato).
- `_grill_sced.py` — protótipo EXPLORATÓRIO (não é a entrega; a implementação oficial, com TDD, é a
  sprint-04 em `student_template.py`). Contém SCED v1/v2/v3, a árvore BST e os geradores de cenário.

---

## Fechamento da sprint-02 (sem consulta prévia ao professor)

**Data:** 2026-10-01. Por restrição de prazo, as perguntas acima **não foram levadas ao professor
antes do envio**. Decisão registrada para a defesa oral:

- **Dúvida 1 (originalidade) — risco aceito, mitigado.** Mantemos o **SCED**. Justificativa: a
  seção 2 do `TP1.md` aceita explicitamente "adaptação estrutural profunda" de técnica conhecida,
  desde que haja (a) identificação clara da origem, (b) descrição das modificações estruturais e
  (c) comparação direta com a literatura — as três condições já estão cumpridas em
  `conceito-autoral.md` §2–3 e §6 (origem = Bingo Sort/NIST DADS; extensão = seleção **bidirecional
  convergente** de dois extremos por passada + análise em função de `d`, não de posição). Isso é
  diferente de "variação cosmética" (critério de nota 0,0), que seria apenas renomear ou reordenar
  um clássico sem extensão estrutural nem declaração. Se o professor divergir dessa leitura na
  arguição, a defesa é: a extensão bidirecional muda a estrutura do algoritmo de forma mensurável
  (⌈d/2⌉ passadas em vez de `d`), não é só maquiagem.
- **Dúvidas 2, 3 e 5** (atalho de já ordenado, convenção de movimentações, estabilidade) ficaram
  para a sprint-03 decidir, já que dependiam de uma escolha de design e não exclusivamente do
  professor — resolvidas em `formalizacao.md`.
- **Dúvida 4** (caminho em árvore) — descartada para esta entrega; mantida apenas como nota
  histórica de exploração (não entra na comparação com a literatura por falta de tempo para
  balanceamento).
- **Dúvida 6** (formato de entrega) — confirmado: Opção B, slides + código executável.
