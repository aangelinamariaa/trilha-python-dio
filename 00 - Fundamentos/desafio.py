menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3


print("Bem vindo ao AMS Sistema Bancário! O que vamos fazer hoje?")
while True:

    opcao = input(menu).lower()

    if opcao == "d":

        valor = input("Informe o valor do depósito sem utilizar separadores decimais: ")

        if not valor.isdigit():
            print("Entrada inválida. Digite apenas números.")
        else:
            if len(valor) == 1:
                valor = float('0.0' + valor)
            else:
                valor = float(valor[:-2] + '.' + valor[-2:])

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor do depósito deve ser maior que zero.")

    elif opcao == "s":
        valor = input("Informe o valor do saque sem utilizar separadores decimais: ")
        
        if not valor.isdigit() and valor != "":
            print("Entrada inválida. Digite apenas números.")
        else:

            if len(valor) == 1:
                valor = float('0.0' + valor)
            else:
                valor = float(valor[:-2] + '.' + valor[-2:])
        
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = qtd_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                print(f"\nSaldo disponível: R$ {saldo:.2f}")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
                print(f"\nLimite máximo por saque: R$ {limite:.2f}")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                print(f"\nLimite de saques diários: {LIMITE_SAQUES}")


            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                qtd_saques += 1
                print("Saque realizado com sucesso!")

            else:
                print("Operação falhou! O valor do saque deve ser maior que zero.")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "x":
        print("Obrigado por utilizar o sistema AMS.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
