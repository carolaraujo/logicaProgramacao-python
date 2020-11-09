# Par ou Ímpar - Python3
Descrição
Escreva um programa em Python 3 que receba um número inteiro não negativo e exiba na dela uma mensagem dizendo se ele é par ou ímpar.

Formato de entrada

A entrada será um número inteiro não negativo (pode ser nulo).
Não é necessário fazer nenhum tipo de validação.
Não exiba nenhum texto para pedir o número para o usuário.
Formato de saída

A saída deverá conter a seguinte mensagem:

O numero <valor> eh par!
quando o número for par, ou:

O numero <valor> eh impar!
quando o número for ímpar.

<valor> é o número dado de entrada
não coloque nenhum acento nas palavras.
Exemplos de:

Entrada

131

Saída

O numero 131 eh impar!

Entrada

26

Saída

O numero 26 eh par!

# Easy Jet
Descrição
A companhia aérea Easy Jet oferece passagens baratas para várias cidades européias e é muito procurada por turistas de todo o mundo. Entretanto, ela tem regras muito rígidas para o tamanho da bagagem de mão de cada cliente: para ser aceita, a mala deve ter no máximo 45 cm de largura, 56 cm de comprimento e 25 cm de altura.

Escreva um programa que receba como entrada as dimensões de uma mala e exiba uma mensagem informando se a mala será aceita ou não.

Formato de entrada

Três valores reais representando largura, comprimento e altura, nesta ordem

Formato de saída

Um String "PERMITIDA" caso a mala esteja dentro das normas da empresa, ou um String "PROIBIDA" caso as dimensões não sejam compatíveis.

Obs: as mensagens devem ser exibidas com as letras todas maiúsculas

Exemplos de:

Entrada

42.9
50
20.2

Saída

PERMITIDA

# Maior, menor ou igual
Descrição
Dados dois números inteiros A e B, exibir:

- 'A eh maior', se A for maior do que B;

- 'B eh maior', se B for maior do que A;

- 'iguais', se os números forem iguais.

Formato de entrada

Na primeira linha o número inteiro correspondente ao A; na segunda linha o número inteiro correspondente ao B.

Formato de saída

A frase 'A eh maior' (sem aspas) ou 'B eh maior' (sem aspas) ou 'iguais' (sem aspas), de acordo com o caso.

Exemplos de:

Entrada

10
20

Saída

B eh maior

Entrada

100
100

Saída

iguais

Entrada

20
10

Saída

A eh maior

# Calculando a contribuição do INSS
Descrição
Na empresa em que você trabalha há muitos funcionários, e às vezes o depósito do INSS é feito incorretamente para alguns deles pois é um processo manual e portanto sujeito a erros. Com isso você decidiu propor a automação de tal processo, para torná-lo mais rápido e reduzir a chance de erros. Escreva um programa que receba o salário base de um funcionário e calcule qual a contribuição devida ao INSS, dada de acordo com a seguinte tabela:
Até R$ 1.751,81 ==> 8%
De R$ 1.751,82 a R$ 2.919,72 ==> 9%
De R$ 2.919,73 até R$ 5.839,45 ==> 11%
Lembrando que esta tabela define um teto para o salário considerado, portanto salários maiores que o salário máximo serão descontados de um valor fixo e igual a 11% do valor do teto.

Formato de entrada

A entrada será um número real, representando o salário base do funcinário.

Formato de saída

A saída deverá ser apresentada no seguinte formato:

Desconto do INSS: R$ 120.00
Onde 120.00 é o valor da contribuição calculado para um salário de 1500.00 reais



Exemplos de:

Entrada

1500

Saída

Desconto do INSS: R$ 120.00

Entrada

2815.72

Saída

Desconto do INSS: R$ 253.41

Entrada

4522.03

Saída

Desconto do INSS: R$ 497.42

Entrada

7567.30

Saída

Desconto do INSS: R$ 642.34

Entrada

2919.73

Saída

Desconto do INSS: R$ 321.17

Entrada

2919.72

Saída

Desconto do INSS: R$ 262.77

# Média e critério de aprovação
Descrição
Escreva um programa que receba as notas e a presença de um aluno, calcule a média e imprima a situação final do aluno.

No semestre são feitas 3 provas, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.

Os critérios para aprovação são:

1 - Frequência mínima de 75%.

2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

E devem ser considerados os casos especiais descritos para a impressão dos resultados, com uma mensagem personalizada para cada situação.

DICA: calcular com uma casa de precisão está associado ao valor que será salvo na memória e não à exibição da resposta, que deve seguir o formato especificado, independentemente de como estamos salvando o valor na memória. Uma coisa é o cálculo e outra a apresentação do resultado.
Ou seja, o valor da média deve ser arredondado para uma casa de precisão antes de serem feitas as verificações que irão decidir se o aluno foi ou não aprovado. Para isso use a função round do Python, que funciona como mostrado no exemplo a seguir.
Essa função recebe 2 parâmetros, o primeiro é o número a ser arredondado e o segundo é o número de casas decimais que queremos:

>>> round(3.765, 1)
3.8
>>> x = 5.3158
>>> round(x, 2)
5.32
Formato de entrada

A entrada serão três números reais no intervalo de 0 a 10, representando as notas do aluno, e um número real no intervalo de 0 a 1 representando a frequência.



Não imprima nenhum texto para pedir os dados ao usuário.

Formato de saída

A saída do programa será um texto com a frequência e a média final do aluno, seguido de uma mensagem referente a sua situação no curso. Exemplo:

Frequencia: 78%
Media final: 6.5
<mensagem>
Se o aluno for reprovado por faltas, a mensagem deve ser: 

Aluno reprovado por faltas!
Caso contrário, temos 4 possibilidades de mensagens:

a) aluno aprovado com média superior a 9 (não inclusivo - não inclui o 9):

Aluno aprovado com louvor!
b) aluno aprovado com média superior a 6 (inclusivo) e inferior a 9 (inclusivo):

Aluno aprovado!
c) aluno reprovado com média superior a 4 (inclusivo) e inferior a 6 (não inclusivo):

Aluno de rec!
b) aluno reprovado com média inferior a 4 (não inclusivo):

Aluno reprovado!
Exemplos de:

Entrada

4
3
6
0.75

Saída

Frequencia: 75%
Media: 4.6
Aluno de rec!

Entrada

3
6
3
0.75

Saída

Frequencia: 75%
Media: 3.9
Aluno reprovado!

Entrada

9.9
10
10
1

Saída

Frequencia: 100%
Media: 10.0
Aluno aprovado com louvor!

Entrada

7
7
7
0.5

Saída

Frequencia: 50%
Media: 7.0
Aluno reprovado por faltas!

Entrada

4
3
6
0.74

Saída

Frequencia: 74%
Media: 4.6
Aluno reprovado por faltas!

Entrada

3.6
2.4
5.3
0.75

Saída

Frequencia: 75%
Media: 4.0
Aluno de rec!