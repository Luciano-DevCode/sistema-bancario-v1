menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
saques = 0
depositos = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Digite o valor de deposito: "))

        if valor>0:
            saldo += valor
            depositos += valor

    elif opcao == "s":
        print("Saque")

        if saldo==0:
            print("Não será possível sacar o dinheiro por falta de saldo!")
        else:
            if numero_saques>=LIMITE_SAQUES:
                print("Limite de 3 saques diários excedido!")
            else:
                saque = float(input("Digite o valor desejado de saque: "))
                if saque>limite:
                    print("Valor acima de R$ 500,00. Saque não permitido!")
                else:
                    if saque>saldo:
                        print("Valor de saldo insuficiente!")
                    else:
                        print("Saque realizado com sucesso!")
                        numero_saques += 1
                        saques += saque
                        saldo -= saque

    elif opcao == "e":
        print("Extrato")

        print(f'''
Depositos (valor total): R${depositos:.2f}
Saques (valor total): R${saques:.2f}
Saldo: R${saldo:.2f}
              ''')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")