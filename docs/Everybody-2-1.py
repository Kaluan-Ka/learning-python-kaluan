#Escreva um programa que solicite o nome de um arquivo, 
#depois abra esse arquivo e percorra todo o seu conteúdo, procurando por linhas no formato:
#X-DSPAM-Confidence: 0.8475
#Conte essas linhas, extraia os valores em ponto flutuante de cada uma delas e calcule a média desses valores, 
#produzindo uma saída conforme mostrado abaixo. Não utilize a função sum() nem uma variável chamada sum na sua solução.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open("mbox-short.txt")
 
 #valores armazenados
total = 0.0
contador = 0

  # Percorre cada linha do arquivo
for line in fh:
    line = line.rstrip()
    # Verifica se a linha começa com "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
    # separa os numeros e faz o float
     continue
    numbers = line[20:40]
    numbers = float(numbers)
    # faz a contagem de itens, a soma dos numeros e calcula a média
    contador = contador + 1
    total = total + numbers
    media = total / contador   
print ("Average spam confidence:" , media)