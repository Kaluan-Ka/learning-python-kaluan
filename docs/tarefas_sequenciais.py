#Exercicio 004
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = input("Primeira Nota")
nota2 = input("Segunda Nota")
nota3 = input("Terceira Nota")
nota4 = input("Quarta Nota")

#tranformar o string em inteiro
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

# soma e faz a media
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4
print (media)

---------------------------------------------------------------

#Exercicio 005
#Faça um Programa que converta metros para centímetros


m = input("Qual é o tamanho em metros ?")
m = float(m)

cm = m*100
print (cm, "cm")

------------------------------------------------------------

#Exercicio 012
#Tendo como dados de entrada a altura de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58

altura = input("Qual sua altura ?")
altura = float(altura)

peso = (72.7*altura) - 58
#tranformar em numero inteiro
peso = int(peso) 

print ("Seu peso ideal é" , peso,"kg")


