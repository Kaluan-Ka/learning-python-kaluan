#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below. 

maior = None
menor = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        #encontrando o maior numero
        if maior is None or number > maior:
            maior = number
        #encontrando menor numero
        if menor is None or number < menor:
            menor = number
    except:
        print("Invalid input")
        continue
    
print("Maximum is", maior)
print ("Minimum is", menor)

