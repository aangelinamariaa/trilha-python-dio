def menu():
    menu_text = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
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

        if opcao == "1": # Depositar
            valor = input("Informe o valor do depósito sem utilizar separadores decimais: ")  
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "2": # Sacar
            valor = input("Informe o valor do saque sem utilizar separadores decimais: ")
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                qtd_saques=qtd_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3": # Exibir Extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4": # Criar cadastro do Usuário
            criar_usuario(usuarios)

        elif opcao == "5": # Criar uma conta para usuário existente
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "6": # Listar contas de um determinado usuário
            listar_contas(usuarios, contas)

        elif opcao == "x":
            print("Obrigado por utilizar o AMS Sistema Bancário! Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(valor, saldo, extrato, /):
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

    return saldo, extrato


def sacar(*, valor, saldo, extrato, limite, qtd_saques, limite_saques):
    if not valor.isdigit() and valor != "":
            print("Entrada inválida. Digite apenas números.")
    else:

        if len(valor) == 1:
            valor = float('0.0' + valor)
        else:
            valor = float(valor[:-2] + '.' + valor[-2:])
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = qtd_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print(f"\nSaldo disponível: R$ {saldo:.2f}")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            print(f"\nLimite máximo por saque: R$ {limite:.2f}")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print(f"\nLimite de saques diários: {limite_saques}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor do saque deve ser maior que zero.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def criar_conta(AGENCIA, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print(f"=== Agência: {AGENCIA} | Conta: {numero_conta:04d} ===")
        return

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
              
def listar_contas(usuarios, contas, AGENCIA="0001"):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return
    
    group = [item for item in contas if usuario['cpf'] == cpf]
    
    if group:
        print(f"\n=== Contas do usuário {usuario['nome']} ===")
        for conta in contas:
            linha = f"""\
            Agência:\t {AGENCIA}
            C/C:\t {conta['numero_conta']:04d}
            """
            print(linha + "\n")

    else:
        print(f"=== {usuario['nome']} não possui contas cadastradas' ===")



main()