#Utilizando o for e realizando uma verificação com o "if"

texto = "danilo"
VOGAIS = "AEIOU"

cont = 0

for letra in texto:
    
    if letra.upper() in VOGAIS:
        cont = cont + 1

print(f"Existem {cont} vogais no texto!")