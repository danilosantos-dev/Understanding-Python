#Entendendo estruturas condicionais em python#
maiorIdade = 18
aptoVotar = 16

idade = int(input("Informe a sua idade:"))

if idade >= maiorIdade:
    print("Você é obrigado a votar, haha!")
elif idade >= aptoVotar and idade < maiorIdade:
    print("Você não é obrigado a votar, mas seria bom!")
else:
    print("Você não pode votar, sinto muito!")

#No python, quando temos uma segunda condição, usamos o elif
#que é a abreviação de else + if, legal né ?

