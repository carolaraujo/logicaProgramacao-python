# Troca de variáveis
Descrição
Complete o código do programa em Python3 que recebe dois valores quaisquer, armazenando-os nas variáveis v1 e v2, e em seguida troca os valores de v1 e v2 e imprime os valores trocados.

Formato de entrada

As entradas poderão ser quaisquer caracteres ou conjuntos de caracteres do teclado.

Formato de saída

A saída devera ser as duas entradas impressas na ordem inversa. Serão impressos os valores armazenados em v1 e v2, nessa ordem, mas o programa deverá ter trocado os valores recebidos em cada variável. (o valor originalmente em v1 passa para v2 e vice-versa).

Código base

# O codigo para a entrada de dados e impressao
# dos resultados eh dado.
v1 = input()
v2 = input()
​
# insira na janela abaixo o codigo responsavel por
# trocar os valores de uma variavel para a outra
//Insira o código aqui
​
print('valor em v1:', v1)
print('valor em v2:', v2)

Exemplos de:

Entrada


1
2

Saída


valor em v1: 2
valor em v2: 1

# Soma de 2 inteiros
Descrição
Escreva um programa em Python3 que receba dois números inteiros e imprima a sua soma.

Formato de entrada

O programa não deve imprimir nenhuma mensagem para pedir os dados de entrada.

Formato de saída

O programa não deve imprimir nenhum outro texto além do resultado numérico.

Exemplos de:

Entrada


2
5

Saída

7
Entrada

-42
53

Saída

11

# Média simples
Descrição
Escreva um programa em Python3 que receba 4 valores, referentes à altura de 4 pessoas, calcule e imprima a média desses valores.

Formato de entrada

As entradas serão números reais positivos não nulos.

Não deve ser impresso nenhum texto para pedir os dados de entrada.
Não é necessário fazer nenhum tipo de validação dos dados de entrada
Formato de saída

A saída devera ser formatada conforme o exemplo:

A media das alturas eh: <valor>
onde <valor> será substituído pelo resultado calculado.

OBS.: Atenção aos acentos no texto de saída.

o The Huxley trabalha com a tabela ASCII, portanto não aceita caracteres acentuados mesmo nas strings (embora o Python aceite pois usa a tabela UTF-8), portanto não use acentos no seu código.


Exemplos de:

Entrada


1.85
1.90
1.63
1.70

Saída

A media das alturas eh: 1.77

# Escalas de temperatura
Descrição
Faça um programa em Python3 que receba uma temperatura em Fahrenheit, calcule e imprima o valor convertido para a escala Celsius e para a escala Kelvin, de acordo com as equações de conversão abaixo:

t_celsius = (t_fahrenheit - 32) * 5/9

t_kelvin = t_celsius + 273.15
Formato de entrada

A entrada será um número real n, com n >= -459.67. (o zero absoluto, ou 0K, é igual a -459.67°F)

Formato de saída

A saída deverá ser formatada conforme o exemplo abaixo:

Convertendo <valor1> graus Fahrenheit temos:
<valor2> graus Celsius e <valor3> Kelvin
Onde valor 1, 2 e 3 são respectivamente os valores de temperatura em Fahrenheit, Celsius e Kelvin.

Notem que na temperatura Kelvin não se usa o termo grau. (Diz-se 250 Kelvin e não 250 graus Kelvin)



[editado] O enunciado e os testes foram editados, removendo-se o símbolo de grau

Exemplos de:

Entrada

212

Saída

Convertendo 212.0 graus Fahrenheit temos:
100.0 graus Celsius e 373.15 Kelvin
Entrada

32

Saída

Convertendo 32.0 graus Fahrenheit temos:
0.0 graus Celsius e 273.15 Kelvin

# Conversão polegadas -> mm
Descrição
Faça um programa em Python3 que receba um valor em polegadas, converta e imprima o resultado em milímetros.

Formato de entrada

A entrada será um número real e não deve ser impresso nenhum texto para pedi-la.

Formato de saída

A saída deverá ser formatada conforme o exemplo:

<valor1> polegada(s) eh o mesmo que <valor2> mm
Onde <valor1> deverá ser substituído pelo valor em polegadas e <valor2> pelo resultado em milímetros. Os números devem ser exibidos sem nenhuma formatação explícita quanto ao número de casas decimais.

OBS.: Atenção aos acentos no texto de saída.

o The Huxley não aceita caracteres acentuados mesmo nas strings

Exemplos de:

Entrada

1

Saída

1.0 polegada(s) eh o mesmo que 25.4 mm