# Conceito Autoral — Ordenação por Seleção Convergente de Extremos Distintos (SCED)

> Artefato da **sprint-02** (Brainstorming). Registra o conceito escolhido, sua intuição,
> hipótese de complexidade e a nota de originalidade. A formalização (pseudocódigo +
> invariante) é a sprint-03; a implementação, a sprint-04.
>
> **Nome provisório:** SCED — *Seleção Convergente de Extremos Distintos*. O aluno pode
> renomear (o nome importa para a apropriação/defesa oral).

**Data:** 2026-09-10 · **Status:** conceito escolhido, aguardando formalização

---

## 1. Intuição / metáfora

Imagine arrumar cartas numeradas espalhadas na mesa. Em vez de comparar carta com carta, você
olha o **conjunto de valores** que existe e trabalha pelas **duas pontas ao mesmo tempo**: numa
varredura você identifica o **menor valor distinto** e o **maior valor distinto** presentes;
recolhe **todas as cópias** do menor e as encosta à esquerda, e **todas as cópias** do maior e
as encosta à direita. Repete no miolo que sobrou, convergindo de fora para dentro, até o miolo
esvaziar (ou virar um único valor).

A ordenação emerge de **percorrer os valores distintos**, não as posições — e de fazê-lo pelos
**dois extremos simultaneamente**.

## 2. Núcleo herdado (declaração de inspiração)

O núcleo — *"selecionar o próximo valor distinto e mover todas as suas repetições de uma vez"* —
é o **Bingo Sort**, uma variante conhecida do Selection Sort (catalogada no NIST/DADS). Assumimos
essa inspiração de forma transparente (ver §6). O Bingo Sort clássico é **unidirecional**:
seleciona só o mínimo por passada.

## 3. Diferencial autoral

A contribuição própria é tornar a seleção **bidirecional e convergente**: cada passada coloca o
**menor E o maior** valor distinto (com todos os seus duplicados) nas duas extremidades da região
ainda não ordenada, usando dois ponteiros que convergem (`esq`, `dir`). Efeitos:

- **~⌈d/2⌉ passadas** em vez de `d` (d = nº de valores distintos).
- Reúne, num só método, as **duas intuições originais do aluno**: (a) agrupar elementos iguais e
  (b) expandir a busca pelos **dois lados** (a simetria da ideia inicial de "±k", agora aplicada
  aos extremos do conjunto de valores em vez de a um passo fixo de valor).
- Frase de defesa: *"não é Bingo Sort — é Bingo Sort com colocação convergente de dois extremos
  distintos por passada"*.

## 4. Esboço de funcionamento (alto nível)

```
enquanto a região [esq..dir] não estiver vazia:
    1. varre [esq..dir] achando o menor valor distinto (vmin) e o maior (vmax)
    2. se vmin == vmax: a região é toda igual → posiciona e encerra
    3. leva todas as cópias de vmin para o bloco esquerdo (avança esq)
       leva todas as cópias de vmax para o bloco direito (recua dir)
    4. repete no miolo que sobrou
direção crescente/decrescente: escolhida pelo usuário (inverte o papel de vmin/vmax)
```

> Detalhe fino a resolver na **sprint-03**: como mover as cópias sem sobrescrever elementos ainda
> não classificados (contagem/troca in-place), e a contagem exata de comparações/movimentações.

## 5. Hipótese de complexidade (a provar na sprint-05)

Seja `n` = tamanho da lista e `d` = número de **valores distintos**.

| Caso | Estimativa | Porquê |
|---|---|---|
| Melhor | **Θ(n)** | poucos valores distintos (ex.: todos iguais → d=1 → 1 passada) |
| Pior | **Θ(n·d) = Θ(n²)** | todos distintos → d = n |
| Médio | **Θ(n·d)** | domina o produto nº de passadas × custo da varredura |
| Espaço | **O(1)** auxiliar (meta) | se conseguirmos a versão in-place por trocas na sprint-03 |

- **Estável:** a definir — depende de como as cópias são movidas (troca vs. deslocamento).
- **In-place:** meta é sim (O(1) extra), a confirmar na formalização.
- Propriedade interessante para a defesa: a complexidade **não** depende do *intervalo* de valores
  (como counting sort) nem é *sempre* n² (como selection sort) — depende de **d**.

## 6. Nota de originalidade

- **Equivalente publicado:** Bingo Sort (NIST DADS) — núcleo idêntico ao concebido pelo aluno de
  forma independente. Complexidade catalogada Θ(n·m)/Θ(n+m²), m = valores distintos.
- **Seleção de dois extremos** (double-ended / cocktail selection) também existe isoladamente.
- **Contribuição autoral = a combinação** (agrupamento de duplicados + colocação convergente
  bilateral) e a análise em função de `d`. Tratamos como **adaptação declarada com extensão
  própria**, não como invenção do zero — postura que protege contra o critério anti-nota-0 e
  concorre ao bônus de uso transparente.

## 7. Riscos / pontos abertos (entram na sprint-03)

1. Provar que a colocação convergente **não corrompe** o miolo (invariante de laço).
2. Definir a movimentação in-place e a **contagem** de comparações/movimentações coerente com o
   contrato `(lista_ordenada, comparacoes, movimentacoes)`.
3. Cobrir bordas: `n=0`, `n=1`, todos iguais, já ordenado, reverso, floats e negativos.
4. Confirmar (ou abrir mão de) estabilidade conforme a estratégia de movimentação.

---

**Referências:** Bingo Sort — NIST Dictionary of Algorithms and Data Structures
(https://xlinux.nist.gov/dads/HTML/bingosort.html). Apostila do projeto: M4 (sorts clássicos),
M5 (recorrências), M6 (estabilidade/in-place).
