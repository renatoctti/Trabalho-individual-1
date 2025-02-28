# Projeto Karatsuba Multiplication

O **Karatsuba Multiplication** é um projeto que implementa o algoritmo de multiplicação de Karatsuba, um método eficiente para multiplicação de números grandes. Ele reduz a complexidade da multiplicação tradicional, tornando-se mais eficiente para entradas grandes.

## Algoritmo de Karatsuba

O algoritmo de Karatsuba é baseado no princípio de dividir para conquistar, quebrando números grandes em partes menores para reduzir o número de multiplicações diretas. Ele segue a seguinte abordagem:

1. Se **x** ou **y** forem menores que 10, retorna **x * y**.
2. Caso contrário:
   - Divide os números em partes menores.
   - Realiza três chamadas recursivas para multiplicação das partes.
     1. **Multiplicação das partes inferiores:**
        ```python
        z0 = karatsuba(low_x, low_y)
        ```
        Multiplica a parte inferior de `x` pela parte inferior de `y`.
     2. **Multiplicação da soma das partes:**
        ```python
        z1 = karatsuba((low_x + high_x), (low_y + high_y))
        ```
        Multiplica a soma das partes superior e inferior de `x` pela soma das partes superior e inferior de `y`.
     3. **Multiplicação das partes superiores:**
        ```python
        z2 = karatsuba(high_x, high_y)
        ```
        Multiplica a parte superior de `x` pela parte superior de `y`.
   - Combina os resultados para formar o produto final.

A complexidade do algoritmo de Karatsuba é **O(n^(log₂(3))) ≈ O(n^1.585)**, que é mais eficiente do que a multiplicação tradicional **O(n²)**.

## Dependências

Este projeto não requer bibliotecas externas, apenas Python 3.

## Versão Pyhton

Versão 3.13.2

## Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado.

2. Clone este repositório:
 ```bash
 git clone https://github.com/renatoctti/Trabalho-individual-1.git
 ```
   
3. O código testa automaticamente diversas combinações de numeros e retorna os resultados. Para rodar o codigo execute o script com o seguinte comando:

```bash
python main.py
```
4. Ao rodar o codigo ele oferece três opções, a primeira e rodar os testes, a segunda é inserir manualmente os números que você quer multiplicar, e a terceira permite que você faça as 2 opções anteriores

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

**Complexidade temporal**

A análise de complexidade temporal estuda o tempo que um algoritmo leva para ser executado em função do tamanho da entrada (n).

Ela avalia quantas operações o algoritmo realiza, e não o tempo exato, já que o tempo pode variar conforme o hardware ou linguagem de programação.

A complexidade temporal do algoritmo de Karatsuba é **O(n^1.585)**, que melhora a abordagem ingênua de multiplicação **O(n²)**. Para grandes valores de `n`, isso reduz significativamente o tempo de execução.

Melhor caso: **O(1)** → Quando os números são menores que 10 (caso base).

Caso médio e pior caso: **O(n^(log2(3))) ≈ O(n^1.585)** → A recursão reduz o tamanho do problema a cada chamada.

A análise temporal mostra que o algoritmo de Karatsuba é mais eficiente que a multiplicação tradicional, especialmente para números grandes, pois reduz o número de multiplicações, mesmo que exija mais somas e subtrações.

**Complexidade Espacial**



A complexidade espacial do algoritmo de Karatsuba depende da profundidade da recursão, em cada chamada, o algoritmo faz 3 chamadas recursivas.

A profundidade da recursão é O(log n) (pois a cada passo os números são reduzidos pela metade).

Levando isto em consideração, a complexidade espacial do algoritmo de Karatsuba não foge de O(log n).

## Complexidade Ciclomática

A complexidade ciclomática é uma métrica usada na engenharia de software para medir a complexidade lógica de um programa, indicando o número de caminhos independentes que existem no código.

A **complexidade ciclomática** é calculada com a fórmula:

\[
M = E - N + 2P
\]

Onde:
- **E** é o número de arestas do grafo de fluxo de controle.
- **N** é o número de nós.
- **P** é o número de componentes conexos (1 para um único programa).

A partir do diagrama, temos:

  **Nós (N) :**
1. Início da função;
2. if x < 10 or y < 10;
3. Return x * y;
4. Cálculo de n;
5. Cálculo de m;
6. Divisão dos números X (divmod);
7. Divisão dos números Y (divmod);
8. Chamada recursiva (z0);
9. Atribuição do resultado a z0;
10. Chamada recursiva (z1);
11. Atribuição do resultado a z1;
12. Chamada recursiva (z2);
13. Atribuição do resultado a z2;
14. Retorno do resultado final;

**Arestas (E) :**

1. Início da função → if x < 10 or y < 10
2. if x < 10 or y < 10 → retorna x * y
3. if x < 10 or y < 10 → Cálculo de n
4. Cálculo de n → Cálculo de m
5. Cálculo de m → Divisão dos números X
6. Divisão dos números X → Divisão dos números Y
7. Divisão dos números Y → Chamada recursiva (z0)
8. Chamada recursiva (z0) → Atribuição do resultado a z0
9. Chamada recursiva (z0) → Início da funçãO
10. Atribuição do resultado a z0 → Chamada recursiva (z1)
11. Chamada recursiva (z1) → Atribuição do resultado a z1
12. Chamada recursiva (z1) → Início da funçãO
13. Atribuição do resultado a z1 → Chamada recursiva (z2)
14. Chamada recursiva (z2) → Atribuição do resultado a z2
15. Chamada recursiva (z2) → Início da funçãO
16. Atribuição do resultado a z2 → Retorno do resultado final



Nós (N): 14

Arestas (E): 16

Componentes conexos (P): 1

Aplicando a fórmula: 

M = 16 - 14 + 2  que resulta 4

A complexidade ciclomática M = 4, indicando um fluxo de controle relativamente simples, mas com recursões que impactam a execução.
## Representação do Fluxo de Controle

O fluxo de controle do algoritmo segue a lógica do diagrama abaixo:





![Diagrama_Karatsuba](https://github.com/user-attachments/assets/38599966-22d6-4a2b-9879-5cf63639cdce)



