import random

#Crie um sistema que o usurio tenha que adivinhar um número entre
#1 e 10, ele terá apenas três chances para acertar!

print("Adivinhe o número que esta entre 1 e 10!")
randomNum = random.randint(1,10)

responseQuant = 0
while responseQuant != 3:
    
    responseUser = int(input("Sua resposta:"))

    if responseUser == randomNum:
        print("Parabéns, você acertou!")
        break    
    else: 
        responseQuant += 1 
    
    
    
    