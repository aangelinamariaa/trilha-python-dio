from desafio_v1 import (
    Cliente,
    Conta,
    Historico,
    Saque,
    Deposito,
    PessoaFisica,
    ContaCorrente
)

def menu():
    menu_text = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [x] Sair

    => """
    return input(menu_text)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    qtd_saques = 0
    numero_conta = 1
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []


    print("Bem vindo ao AMS Sistema Bancário! O que vamos fazer hoje?")
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor = input("Informe o valor do depósito sem utilizar separadores decimais: ")  
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque sem utilizar separadores decimais: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                qtd_saques=qtd_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "x":
            print("Obrigado por utilizar o AMS Sistema Bancário! Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(valor, saldo, extrato, /):
    dep = Deposito(valor)
    if dep:
        print("Depósito realizado com sucesso!")
    return saldo, extrato


def sacar(*, valor, saldo, extrato, limite, qtd_saques, limite_saques):
    conta = Conta(None, None)
    saq = conta.sacar(valor=valor)
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    extrato = Historico()
    print (extrato.transacoes)

def criar_usuario(usuarios):
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o CPF (somente número): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cli = Cliente(endereco)

    cli_pf = PessoaFisica(nome, data_nascimento, cpf, endereco)
    if cli_pf:
        print("=== Usuário criado com sucesso! ===")

def criar_conta(AGENCIA, numero_conta, usuarios, contas):
    nc = Conta(numero_conta, None)

    nc_cc = ContaCorrente(nc, None)
    if nc_cc:
        print("=== Conta criada com sucesso! ===")
              
main()
