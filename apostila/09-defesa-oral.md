# M9 — Guia de Defesa Oral

**Objetivo:** Preparar-se para a arguição respondendo às perguntas prováveis e garantindo que
nada cause nota 0,0. Use este módulo como roteiro de ensaio antes da apresentação.

---

## Checklist anti-nota-0 (verificar antes de entregar)

- [ ] `python test_suite.py` roda 100% dos 10 cenários (6 classes × 10 testes) sem falha
- [ ] Declaração de IA presente e completa (ferramenta, por quê, como, o que foi modificado, como validado)
- [ ] Código executável entregue e reproduz os experimentos
- [ ] Algoritmo **não** é variação cosmética de clássico (verifique: qual diferencial real ele tem?)
- [ ] Slides cobrem todos os itens obrigatórios do M0

---

## Perguntas prováveis — e como responder

### Sobre o algoritmo

**"Explique a intuição do seu algoritmo sem usar notação matemática."**

Prepare uma metáfora concreta (ex: "é como organizar cartas dividindo por naipe antes de
ordenar cada naipe"). A intuição deve ser compreensível sem nenhuma fórmula.

**"Por que seu algoritmo não é apenas uma variação do [Bubble/Insertion/Quick Sort]?"**

Identifique o diferencial estrutural — uma propriedade que os clássicos não têm. Se não
conseguir nomear isso em 30 segundos, a ideia precisa ser repensada.

**"Qual é o caso que mais prejudica seu algoritmo? Consegue construir esse caso?"**

Construa um vetor concreto que force o pior caso e mostre os números de comparações.

---

### Sobre o invariante de laço

**"Enuncie o invariante de laço do seu algoritmo."**

Deve ser uma frase precisa: "No início da iteração k, o subvetor [0..k-1] satisfaz a
propriedade P".

**"Mostre a inicialização do invariante."**

Para k=0 (ou k=1), mostre que P vale trivialmente. Ex: "vetor de 0 elementos está
vacuamente ordenado."

**"Como a iteração k mantém o invariante para k+1?"**

Explique passo a passo por que, se P vale antes da iteração, então P ainda vale depois.

**"O término do laço implica que a lista está ordenada?"**

Ao final, k = n. Se o invariante diz que [0..k-1] está ordenado e k=n, então [0..n-1]
está ordenado. Conecte explicitamente.

---

### Sobre complexidade

**"Qual é a complexidade de tempo no pior caso? Prove."**

Não diga apenas "O(n log n)". Mostre: "no pior caso, o laço externo executa n vezes e o
interno executa k vezes, logo T(n) = ...".

**"Por que seu algoritmo não pode ser melhor que Ω(n log n) no pior caso?"**

Resposta padrão: "Qualquer algoritmo de ordenação por comparação é Ω(n log n) no pior caso,
pela prova da árvore de decisão (CLRS Cap. 8.1). Como meu algoritmo usa apenas comparações,
está sujeito a esse limite."

**"Os dados empíricos do benchmark confirmam sua análise teórica?"**

Mostre o gráfico de comparações × N e aponte: "a curva segue a forma de [n², n log n],
consistente com a complexidade teórica O(...)".

**"Qual é o espaço auxiliar?"**

Responda com O(1) se in-place, O(n) se usar espaço extra, O(log n) se recursivo.

---

### Sobre estabilidade

**"Seu algoritmo é estável?"**

Se sim: "Sim. O critério de comparação nunca troca elementos iguais de posição. Especificamente,
[mostre a linha do código onde a comparação é estrita: `<` e não `<=`]."

Se não: "Não. Aqui está um contra-exemplo: [entrada concreta onde dois elementos iguais
trocam de posição]."

---

### Sobre o código

**"Por que seu sort retorna 3 valores?"**

"O contrato do TP1 exige `(lista_ordenada, comparações, movimentações)` para permitir análise
empírica uniforme comparando todos os algoritmos."

**"O que acontece se a lista de entrada for vazia ou tiver um único elemento?"**

Mostre no código que esses casos são tratados e que o retorno é `([], 0, 0)` e `([x], 0, 0)`.

**"Como você validou que o algoritmo está correto?"**

"`python test_suite.py` — 10 cenários incluindo vazio, unitário, reverso, duplicatas, floats
e negativos. Todos passam."

---

### Sobre o uso de IA

**"Como você usou IA neste trabalho?"**

Leia sua declaração de IA. Você deve saber explicar: qual ferramenta, para quê (apostila?
brainstorming? revisão?), o que foi modificado por você e como validou que o resultado é correto.

**"A ideia do algoritmo foi gerada pela IA?"**

Se sim, declare transparentemente. Se não, explique qual foi a sua contribuição intelectual.
Declaração transparente concorre ao bônus "Uso Excepcional de IA".

---

## Roteiro de ensaio (30 minutos)

1. Leia os slides do começo ao fim sem parar — identifique onde você travaria.
2. Cubra os slides e explique o algoritmo em voz alta, só com a metáfora.
3. Escreva o invariante de memória em papel, sem consultar.
4. Execute mentalmente o algoritmo em `[5, 3, 1, 4, 2]` — confira com o código.
5. Responda em voz alta as 10 perguntas desta seção.

---

## Referências (para citar na defesa)

- **CLRS Cap. 2.1** — invariante de laço (Insertion Sort)
- **CLRS Cap. 3** — notação assintótica
- **CLRS Cap. 8.1** — limite inferior Ω(n log n)
- **Sedgewick & Wayne** — análise empírica e tabelas comparativas
- Código do pacote: `classical.py`, `test_suite.py`, `benchmark.py`
