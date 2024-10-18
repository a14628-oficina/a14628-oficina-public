valorA = input("Insira uma valor de 1 - 10: ")
print(valorA)

#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos.");

#EX0.2:
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá Mundo");
fruta = "Melancia"
print(f"Eu gosto de {fruta}.")

#EX0.3:
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Insira o meu nome: ")
print(f"Bom dia, {nome}, desejo um excelente dia de trabalho!")
valor = int(input("Insira um numero: "))
dobro = valor * 2
print(f"O dobro de {valor} é {dobro}")

#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print("\nBem-Vindos ao Python!")

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
print("\nRodrigo, bem-vindo ao Python!")

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
mensagem = """  ________  ________  _____ ______           ________  ___  ________     
|\   __  \|\   __  \|\   _ \  _   \        |\   ___ \|\  \|\   __  \    
\ \  \|\ /\ \  \|\  \ \  \\\__\ \  \       \ \  \_|\ \ \  \ \  \|\  \   
 \ \   __  \ \  \\\  \ \  \\|__| \  \       \ \  \ \\ \ \  \ \   __  \  
  \ \  \|\  \ \  \\\  \ \  \    \ \  \       \ \  \_\\ \ \  \ \  \ \  \ 
   \ \_______\ \_______\ \__\    \ \__\       \ \_______\ \__\ \__\ \__\
    \|_______|\|_______|\|__|     \|__|        \|_______|\|__|\|__|\|__|"""
print(mensagem)

#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""

nome = "Rodrigo Cardoso"
idade = int("15")
localidade = "famalicao"

print(f"{nome}, tem {idade} anos e reside em {localidade}")

#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""

linguagemprog = "Python"
nome = "Rodrigo Cardoso"

print(f"O {nome} sabe programar em {linguagemprog}")

#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
print(f"{'Bem-vindo ao Python!' : <50} ")
print(f"{'Bem-vindo ao Python!' : ^50} ")
print(f"{'Bem-vindo ao Python!' : >50} ")

#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""

raio = float(input("Insira o raio da circunferencia : "))
perimetro = 2 * 3.14 * raio
area = 3.14*((raio)**2)
print("Uma circunferência do raio: ",raio,"unidades,")
print("tem um comprimento de : ",perimetro,"unidades")
print("e área de: ",area,"unidades")

#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""

from dataclasses import make_dataclass
import datetime
x = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}/{dia}/{ano}")
print(f"{hora}:{minutos}:{segundos}")

#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""

print("Digite o numero do atleta: 14628")
print("Digite a pontuação final: 7.89")
print("O atleta número 14628 obteve 7.89 pontos.")

#EX1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""

import datetime

print("Digite a data de nascimento: 05-07-2009 ")
data_nascimento = datetime.datetime(2009, 7, 5)
data_atual = datetime.datetime.now()
idade = data_atual - data_nascimento
print("A idade é:", idade)
print("Digite o dia:05 ")
print("Digite o mes:07 ")
print("Digite o ano:2009 ")

nome = str(input('Qual é seu nome? '))
if nome == 'Rodrigo':
  print('Que nome lindo tu tens!')
else:
  print('O teu nome é tão comum')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2 )/2
print('A tua média foi {:.1f}'.format(m))
if m >= 6.0:
  print('A tua média foi boa! PARABÉNS!')
else:
  print('A tua média foi má! ESTUDA MAIS!')

#A028

import random  

segredo = int(random.randint(0, 5))
print(f"o numero secreto é : {segredo}")

numeroescolhido = int(input("Insira um valor entre (0 e 5): "))

if numeroescolhido > segredo:
  print("O número inserido é maior do que o meu!")
elif numeroescolhido < segredo:
  print("O número inserido é menor do que o meu!")
else:
 print("Acertaste!")

  #A029

velocidade = int(input("Insira a velocidade em que estava: "))
multa = velocidade - 80
 valor = ( multa) *7 
  if velocidade >80:
 print (f"Excedeste a velocidade em {multa}km/h e vais ter de pagar {valor} €")
  else:
print ("Estavas na velocidade certa!")

 #2. Exercícios
"""
 Exercício FP1: Verificar se um número é positivo, negativo ou zero.
 Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
 Dica: Usa as estruturas condicionais if, elif e else.

 [consola]
 Introduza um número: 10
 O número é positivo.
"""
numero = int(input("Insira um numero: "))
if numero == 0:
  print("O numero é zero")
elif numero < 0:
  print("O numero é negativo")
elif numero > 0: 
 print("O numero é positivo")

  #Exercício FP2: 
"""
Verificar se um número é par ou ímpar.
  Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
  Dica: Para verificar se um número é par, utilize a operação de módulo %.

  [consola]
  Introduza um número: 7
  O número é ímpar.
"""

x = numero = int(input("Insira o número: "))
resultado = x % 2

if resultado != 0:
 print("O número inserido é Impar!")
else:
 print("O número é Par ")

#Exercício FP3: 
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"

[consola]
Introduza a nota final: 16
Classificação: Bom
"""

  notafinal = int(input("Insira a Nota final do aluno: "))

  if notafinal < 10:
    print("Reprovado")
  elif notafinal >= 10 and notafinal <= 14:
     print("Suficiente")
  elif notafinal >= 15 and notafinal < 17:
    print("Bom")
  else:
    print("Muito Bom")

#Exercício FP4:
"""
Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15

Introduza a temperatura em Celsius: 25
Deseja converter para (F) Fahrenheit ou (K) Kelvin? F
A temperatura em Fahrenheit é: 77.0°F

"""

Celsius = float(input("Insira a temperatura em graus Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15
opcao = str(input("Escolha a conversão para Fahrenheit(F), Kelvin(K) ou Ambas(A)"))
if opcao == "F":
  print (f"O valor em Fahrenheit é {Fahrenheit}")
elif opcao == "K":
 print (f"O valor em Kelvin é {Kelvin}")
elif opcao == "A":
  print (f"O valor em Fahrenheit E {Fahrenheit} e me Kelvin E {Kelvin}")
else:
 print ("Opção Inválida")

#Exercício FP5:
"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.

[consola]
Introduza o seu salário: 2500
Salário após impostos: 2000.0
"""

salario = float(input("Insira o seu salário mensal: "))
if salario < 1000 :
  print("O seu imposto é zero isento de imposto")
elif salario > 1000 and salario < 2000 :
  imposto1 = salario * 0.10
  salarioImposto = salario - imposto
  print(f"Oseu salario mensal com o imposto de 10% é de: {salarioImposto}")
elif salario >= 2000 :
  imposto = salario * 0.20
  salarioImposto = salario - imposto
  print(f"Oseu salario mensal com o imposto de 20% é de: {salarioImposto:.2f}€")
  
numeros = [1,2,3]
turma1I = ["Rodrigo", "Costa", "Cardoso"]
for x in numeros:
  for y in turma1I:
    print(y,x)

#Exercício FP6:
"""
Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.

[consola]
1
2
3
...
10
"""
for x in range(1,11):
  print(x)

#Exercício FP7:
"""
Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

[consola]
A soma de 1 a 100 é: 5050
"""

i = 1
soma = 0
while i <= 100:
  soma += i 
  i += 1
  print(soma)

soma = 0 
i = 1
while i <= 100:
  soma += i 
  i += 1
print(f"A soma de 1 a 100 é: {soma}")


#Exercício FP8:
"""
Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.

[consola]
Introduza uma frase: Programação em Python
Número de vogais: 7
"""

frase = input("Insira uma frase: ")
vogais = 0

for letra in frase:
  if letra  == "a" or letra == "e" or letra == "i" or letra ==  "o" or letra == "u" == letra  == "A" or letra == "E" or letra == "I" or letra ==  "O" or letra == "U":
    vogais += 1

print(vogais)

#Exercício FP9:
"""
Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.

[consola]
5
10
15
...
50
"""
temporario = 0
for i in range(1,51):
  if temporario <= 49:
     temporario = i * 5
     print(temporario)


#Exercício FP10:
"""
Verificar se um número é primo.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.

[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0
"""

#1.

numeros = []
for i in range(5):
   numero = int(input(f"Insira o número: "))
   numeros.append(numero)
media = sum(numeros) / ler(numeros)
print(f"A média é: {media}")

#2.

notas = []
for i in range(0,5):
 numeros = int(input("Insira um valor inteiro: "))
 notas.append(numeros)
soma = sum(notas)
valor1 = notas[0]
print(valor1)
x = len(notas)
media = (soma/x)
print(media)

#Exercício FP11:
"""
Verificar se um número é primo.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.

[consola]
Introduza um número: 13
13 é um número primo.

RESOLUÇÃO

"""

numero = int(input('Insira um numero: '))
divisores = 0
for i in range(1, numero + 1 ):
    if numero % i == 0: #verifica se o resultado da divisão é 0 
        divisores += 1  #incrementa o contador de divisores
if divisores  == 2:
    print(f"O {numero} é um número primo")
else:
    print(f"O {numero} não é um número primo")


#Exercício FP12:
"""
Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

[consola]
Lista de números pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""

lista = []
for i in range(1,21):
  if i % 2 == 0:
    lista.append(i)
print(f"Lista de numeros pares: {lista}")

#Exercício FP13:
"""
Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.

[consola]
Introduza uma palavra: Python
A palavra invertida é: nohtyP
"""

texto = str(input("Insira um texto: ")) #Pedir  o texto ao utilizador
textoinv = texto [::-1] #Script para inverter o texto 
print(textoinv) #Printar o texto invertido         

#Exercício FP14: 
"""
Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

[consola]
Introduza um número: 6
Tabuada de 6:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
"""


num = int(input("Introduza um número: "))
for i in range(1,11):
  mult = num * i 
  print(f"{num} x {i} = {mult}")


num = int(input("Introduza um numero: "))
i = 1
while i <11:
  mult = num * i 
  print(f"{num} x {i} = {mult}")
  i += 1
