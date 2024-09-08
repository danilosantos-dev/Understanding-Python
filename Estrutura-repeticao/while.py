#Utilizando o "while" a repetição irá acontecer apenas em quanto a condição 
#criada for verdadeira, no caso abaixo True sempre será verdadeiro até alguma condição encerrar o sistema.

print("0-Sair, 1-Sacar todo dinheiro, 2-Depositar grana, 3-Transferir saldo em conta ")

while True:
    
    opcao = int(input("Opção:"))

    if opcao == 0:
        break
    elif opcao == 1:
        print("Sacou toda grana!")
        break
    elif opcao == 2:
        print("Depositou toda a grana!")
        break
    elif opcao == 3:
        print("Transferiu toda a grana!")
        break
    else:
        print("Selecione uma opcao valida!")