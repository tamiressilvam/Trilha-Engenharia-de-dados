menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0 :
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}/n"

        else :
            print("Operação não realizada! O valor informado é inválido.")
    
    elif opcao == "s":
       valor = float(input("Informe o valor do  saque :"))

       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saques =  numero_de_saques >= LIMITE_DE_SAQUES

       if excedeu_saldo:
           print("Operação não realizada! Você não possui saldo suficiente.")

       elif excedeu_limite:
           print("Operação não realizada! O valor de saque excede o limite.")

       elif excedeu_saques:
           print("Operação não realizada! Número de saques excedidos.")

       elif valor > 0 :
           saldo -= valor 
           extrato +=  f"Saque: R$ {valor:.2f}/n"
           numero_de_saques += 1

       else:
           print("Operação não realizada! O valor informado é invalido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada novamente.")
