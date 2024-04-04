#!/usr/bin/env python3
"""Sistema bancário V1"""

__version__ = "v0.1.0"
__author__ = "Carlos Moreno"

menu = """\
[d/D] Deposito
[s/S] Saque
[e/E] Extrato
[q/Q] Sair

==> """

saldo = 0
LIMITE = 500
extrato = []
qtd_saques_dia = 0
msg_saldo = "Saldo: R$ %(saldo).2f\n"
QTD_LIMITE_SAQUE = 3


def depositar():
    saldo = globals().get("saldo")
    print(" Operação de Deposito ".center(50, "="))
    valor = float(input("Informe o valor do deposito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"C(+)\t{valor}")
    print(f"Deposito no valor de {valor:.2f} realizado com sucesso!")
    return saldo


def sacar():
    saldo = globals().get("saldo")
    QTD_LIMITE_SAQUE = globals().get("QTD_LIMITE_SAQUE")
    qtd_saques_dia = globals().get("qtd_saques_dia")
    LIMITE = globals().get("LIMITE")
    extrato = globals().get("extrato")

    print(" Operação de Saque ".center(50, "="))
    valor = float(input("Informe o valor a ser sacado: "))

    if (
        (valor <= saldo)
        and (valor <= 500)
        and qtd_saques_dia < QTD_LIMITE_SAQUE
    ):
        saldo -= valor
        qtd_saques_dia += 1
        extrato.append(f"D(-)\t{valor}")
        print(f"Saque no valor de {valor:.2f} realizado com sucesso!")
        print(
            f"Você ainda possui {QTD_LIMITE_SAQUE - qtd_saques_dia} "
            f"saque(s) no dia no valor de R$ {LIMITE}"
        )
    else:
        print("Saque inválido!")
        print(
            "OBS.: O valor solicitado deve ser menor ou igual ao saldo "
            f"atual de {saldo:.2f} e menor ou igual a que R$ 500"
        )
    return saldo


def obter_extrato():
    extrato = globals().get("extrato")
    saldo = globals().get("saldo")
    print(" Extrato ".center(50, "="))
    print("\n".join(extrato))
    print(f"\nSaldo: {saldo:.2f}")
    print("".center(50, "="))


while True:
    print(" Opções ".center(50, "="))
    opcao = input(menu).lower()

    if opcao == "d":
        saldo = depositar()
    elif opcao == "s":
        saldo = sacar()
    elif opcao == "e":
        obter_extrato()
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecione uma das opções listadas!")
