#Esse codigo escolhe 6 numeros de 1 a 60 aleatoriamente e diz quais numeros foram os mais escolhidos nas tentativas impares.

import random

# Lista para armazenar os números das tentativas ímpares
numeros_impares = []

# Fazer 100 tentativas
for tentativa in range(1, 101):
    # Escolher 6 números aleatórios entre 1 e 60
    numeros = random.sample(range(1, 61), 6)
    
    # Se for tentativa ímpar, guardar os números
    if tentativa % 2 != 0:
        numeros_impares.extend(numeros)
        print(f"Tentativa {tentativa}: {sorted(numeros)}")

print("\n" + "="*50)
print("NÚMEROS ESCOLHIDOS NAS TENTATIVAS ÍMPARES:")
print("="*50)

# Contar frequência de cada número
from collections import Counter
frequencia = Counter(numeros_impares)

# Mostrar os números e quantas vezes apareceram
print("\nNúmeros e suas frequências:")
for numero, vezes in sorted(frequencia.items()):
    print(f"Número {numero:2d}: apareceu {vezes} vezes")

# Mostrar os 6 números mais frequentes
print("\n" + "="*50)
print("OS 6 NÚMEROS MAIS SORTEADOS:")
print("="*50)
mais_frequentes = frequencia.most_common(6)
for numero, vezes in mais_frequentes:
    print(f"Número {numero}: {vezes} vezes")
