# Projeto Karatsuba Multiplication

O **Karatsuba Multiplication** é um projeto que implementa o algoritmo de multiplicação de Karatsuba, um método eficiente para multiplicação de números grandes. Ele reduz a complexidade da multiplicação tradicional, tornando-se mais eficiente para entradas grandes.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é baseado no princípio de dividir para conquistar, quebrando números grandes em partes menores para reduzir o número de multiplicações diretas. Ele segue a seguinte abordagem:

1. Se **x** ou **y** forem menores que 10, retorna **x * y**.
2. Caso contrário:
   - Divide os números em partes menores.
   - Realiza três chamadas recursivas para multiplicação das partes.
   - Combina os resultados para formar o produto final.

A complexidade do algoritmo de Karatsuba é **O(n^(log2(3))) ≈ O(n^1.585)**, que é mais eficiente do que a multiplicação tradicional **O(n²)**.

## Dependências

Este projeto não requer bibliotecas externas, apenas Python 3.

## Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado.
2. Execute o script com o seguinte comando:

```bash
python main.py
```
3. Este projeto inclui testes automatizados com **unittest**. Para executá-los, utilize:

```bash
python -m unittest main.py
```

## Explicação do código

### Arquivo: main.py

- **Objetivo:** Implementa o algoritmo de Karatsuba para multiplicação eficiente.
- **Descrição da função principal:**

#### `karatsuba(x, y)`
- **Parâmetros:**
  - `x`: Número inteiro.
  - `y`: Número inteiro.
- **Retorno:**
  - O produto de `x` e `y` calculado usando o método de Karatsuba.

### Fluxo de execução:
1. Verifica se **x** ou **y** são menores que 10.
2. Se forem, retorna diretamente o produto.
3. Caso contrário:
   - Divide `x` e `y` em partes menores (high e low).
   - Calcula três multiplicações recursivas:
     - `z0 = karatsuba(low_x, low_y)`
     - `z1 = karatsuba(low_x + high_x, low_y + high_y)`
     - `z2 = karatsuba(high_x, high_y)`
   - Combina os resultados e retorna o produto final.

## Analise da Complexidade Assintótica

A complexidade temporal do algoritmo de Karatsuba é **O(n^1.585)**, que melhora a abordagem ingênua de multiplicação **O(n²)**. Para grandes valores de `n`, isso reduz significativamente o tempo de execução.

Melhor caso: **O(1)** → Quando os números são menores que 10 (caso base).

Caso médio e pior caso: **O(n^(log2(3))) ≈ O(n^1.585)** → A recursão reduz o tamanho do problema a cada chamada.

## Complexidade Ciclomática

A **complexidade ciclomática** é calculada com a fórmula:

\[
M = E - N + 2P
\]

Onde:
- **E** é o número de arestas do grafo de fluxo de controle.
- **N** é o número de nós.
- **P** é o número de componentes conexos (1 para um único programa).

A partir do diagrama, temos:

Nós (N): 9

Arestas (E): 10

Componentes conexos (P): 1

Aplicando a fórmula: 

A complexidade ciclomática M = 3, indicando um fluxo de controle relativamente simples, mas com recursões que impactam a execução.
## Representação do Fluxo de Controle

O fluxo de controle do algoritmo segue a lógica do diagrama abaixo:

![Diagrama de Fluxo](caminho_para_o_diagrama.png)

