#!/usr/bin/env python3
"""Sistema bancário V2"""

__version__ = "v0.2.0"
__author__ = "Carlos Moreno"

usuarios = dict()
contas = dict()

opcoes = """\
  [c/C] Cadastrar Conta
  [d/D] Depositar
  [e/E] Exibir Extrato
  [l/L] Listar Usuários
  [s/S] Sacar
  [u/U] Cadastrar Usuário
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


def main():
    while True:
        print(" Menu ".center(50, "="))

        match input(opcoes).lower():
            case "c":
                ...
            case "d":
                ...
            case "e":
                ...
            case "l":
                print(" Usuários Cadastrados no Sistema ".center(50, "="))
                resultado = listar_usuarios()
                print(resultado)
            case "s":
                ...
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
