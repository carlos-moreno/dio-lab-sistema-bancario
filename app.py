#!/usr/bin/env python3
"""Sistema bancário V2"""

from random import randint

__version__ = "v0.2.0"
__author__ = "Carlos Moreno"

usuarios = dict()
contas = dict()
extratos = dict()
saldos = dict()
limites_saque = dict()
AGENCIA = "0001"

opcoes = """\
  [c/C]   Cadastrar Conta
  [d/D]   Depositar
  [e/E]   Exibir Extrato
  [lc/LC] Listar Contas
  [lu/LU] Listar Usuários
  [s/S]   Sacar
  [u/U]   Cadastrar Usuário
==> """


def cadastrar_usuario(
    nome: str, data_nascimento: str, cpf: str, endereco: str
) -> str:
    """Cadastrar usuários no sistema.

    A função `cadastrar_usuario` tem a finalizadade de cuidar do cadastro de
    novos usuários no sistema, tornando-os aptos a usar todas as
    funcionalidades disponíveis no sistema, como por exemplo: depositar,
    sacar e exibir o extrato da conta.

    Parameters
    ----------
        nome: str
            Nome do futuro cliente
        data_nascimento: str
            Data de Nascimento do futuro cliente
        cpf: dict
            CPF do futuro cliente
        endereco: str
            Endereço do futuro Cliente

    Returns
    -------
        str
    """

    resultado = "\nUsuário já cadastrado!"
    if usuarios.get(cpf) is None:
        usuarios[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }
        resultado = (
            f"\nUsuário {usuarios.get(cpf).get('nome')} "
            "cadastrado com sucesso!"
        )
    return resultado


def listar_usuarios():
    """Listar os usuários cadastros no sistema.

    A função `listar_usuarios` tem a finalizadade de cuidar da listagem de
    todos os usuários que estão cadastrados no sistema.

    Parameters
    ----------

    Returns
    -------
        str
    """

    l = []
    for key in usuarios.keys():
        nome = usuarios.get(key).get("nome")
        cpf = key
        data_nascimento = usuarios.get(key).get("data_nascimento")
        endereco = usuarios.get(key).get("endereco")
        l.append(
            f"Nome: {nome}\nCPF: {cpf}\nData de Nascimento: {data_nascimento}"
            f"\nEndereço: {endereco}"
        )

    return "\n#####\n".join(l)


def cadastrar_conta(usuario: str, agencia=AGENCIA) -> str:
    """Cadastrar conta no sistema.

    A função `cadastrar_conta` tem a finalizadade de cuidar do cadastro de
    uma nova conta bancária no sistema, fazendo a ligação entre os usuários
    cadastrados no sistema e uma conta para realizar as devidas movimentações
    disponíveis no sistema, como por exemplo: depositar, sacar e exibir o
    extrato da conta.

    Parameters
    ----------
        usuario: str
            CPF do Cliente a ser registrado na conta
        agencia: str
            Agência da nova conta, por padrão a agência "0001" é usada

    Returns
    -------
        str
    """
    numero_conta = str(randint(1, 999999999)).zfill(9)
    contas[numero_conta] = {"usuario": usuario, "agencia": agencia}
    resultado = (
        f"\nConta {numero_conta} criada com sucesso para o usuário "
        f"{contas.get(numero_conta).get('usuario')}."
    )
    return resultado


def listar_contas():
    """Listar as contas cadastras no sistema.

    A função `listar_contas` tem a finalizadade de cuidar da listagem de
    todas as contas que estão cadastrados no sistema.

    Parameters
    ----------

    Returns
    -------
        str
    """

    l = []
    for key in contas.keys():
        nome = usuarios.get(contas.get(key).get("usuario")).get("nome")
        numero_conta = key
        agencia = contas.get(key).get("agencia")
        l.append(
            f"Nome: {nome}\nNúmero da Conta: {numero_conta}"
            f"\nAgência: {agencia}"
        )

    return "\n#####\n".join(l)


def depositar(conta: str, valor: float) -> str:
    """Depositar saldo na conta.

    A função `depositar` tem a finalizadade de cuidar do depósito de saldo
    na conta bancária do cliente.

    Parameters
    ----------
        conta: str
            Conta do Cliente onde o saldo vai ser adicionado
        valor: float
            Valor a ser depositado

    Returns
    -------
        str
    """
    extratos.setdefault(conta, []).append(f"D(+)    {valor:.2f}")
    saldo = float(valor)
    if saldos.get(conta):
        saldo = float(saldos.get(conta))
        saldo += float(valor)
    saldos[conta] = saldo
    return (
        f"Deposito no valor de R$ {valor:.2f} para a conta {conta} realizado "
        "com sucesso!"
    )


def sacar(conta: str, valor: float) -> str:
    """Sacar valor da conta.

    A função `sacar` tem a finalizadade de cuidar dos saques na conta
    bancária do cliente.

    Parameters
    ----------
        conta: str
            Conta do Cliente onde o saldo vai ser adicionado
        valor: float
            Valor a ser sacado
        limite: int
            Limite de saques

    Returns
    -------
        str
    """
    saldo = float(saldos.get(conta))
    tem_saque_disponivel = bool(
        limites_saque.get(conta) is None
        or (
            limites_saque.get(conta) is not None
            and limites_saque.get(conta) <= 3
        )
    )
    valor_permitido = (valor <= 500) and (valor <= saldo)
    if tem_saque_disponivel and valor_permitido:
        extratos.setdefault(conta, []).append(f"C(-)    {valor:.2f}")
        saldo -= float(valor)
        saldos[conta] = saldo
        print(saldos)
        return f"Saque no valor de R$ {valor:.2f} da conta {conta} realizado com sucesso!"
    elif tem_saque_disponivel is False:
        return "Quantidade de saques excedidas no dia!"
    elif valor_permitido is False:
        return f"Valor a ser sacado deve ser menor que R$ 500 e menor ou igual a R$ {saldo}"


def main():
    while True:
        print(" Menu ".center(50, "="))

        match input(opcoes).lower():
            case "c":
                msg = (
                    "Cadastrando uma Nova Conta, por favor, preencha os "
                    "dados solicitados a seguir."
                )
                print(msg)
                usuario = input(
                    "Informe o CPF do Usuário a ser cadastrado na conta: "
                )
                if usuarios.get(usuario) is not None:
                    resultado = cadastrar_conta(usuario=usuario)
                    print(resultado)
                else:
                    print(
                        f"O usuário com CPF {usuario} não foi encontrado, "
                        "verifique o dado informado e tente novamente"
                    )
            case "d":
                msg = (
                    "Para o procedimento de Deposito, por favor, preencha os "
                    "dados solicitados a seguir."
                )
                print(msg)
                conta = input(
                    "Informe a Conta do Usuário a ser depositado o valor: "
                )
                valor = float(input("Qual o valor a ser depositado: "))
                if contas.get(conta) is not None:
                    resultado = depositar(conta, valor)
                    print(resultado)
                else:
                    print(
                        f"A Conta {conta} informada para deposito não existe!"
                    )
            case "e":
                print(extratos)
            case "lc":
                print(" Contas Cadastradas no Sistema ".center(50, "="))
                resultado = listar_contas()
                print(
                    resultado
                    if resultado
                    else "Nenhum Conta cadastrada no sistema.\n"
                )
            case "lu":
                print(" Usuários Cadastrados no Sistema ".center(50, "="))
                resultado = listar_usuarios()
                print(
                    resultado
                    if resultado
                    else "Nenhum Usuário cadastrado no sistema.\n"
                )
            case "s":
                msg = (
                    "Para o procedimento de Saque, por favor, preencha os "
                    "dados solicitados a seguir."
                )
                print(msg)
                conta = input(
                    "Informe a Conta do Usuário a ser sacado o valor: "
                )
                valor = float(input("Qual o valor a ser sacado: "))
                if contas.get(conta) is not None:
                    resultado = sacar(conta, valor)
                    print(resultado)
                else:
                    print(f"A Conta {conta} informada para saque não existe!")
            case "u":
                msg = (
                    "Cadastrando um Novo Usuário, por favor, preencha os "
                    "dados solicitados a seguir."
                )
                print(msg)
                nome = input("Nome: ")
                cpf = input("CPF (formato 99999999999): ")
                data_nascimento = input("Data de Nascimento: ")
                endereco = input("Endereço: ")
                resultado = cadastrar_usuario(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    cpf=cpf,
                    endereco=endereco,
                )
                print(resultado)
            case "q":
                break
            case _:
                msg = (
                    "Opção inválida, por favor selecione uma das opções "
                    "listadas!"
                )
                print(msg)


if __name__ == "__main__":
    main()
