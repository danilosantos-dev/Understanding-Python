#Muito utilizada em condicões simples de uma unica linha

saque = 200
saldo = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")