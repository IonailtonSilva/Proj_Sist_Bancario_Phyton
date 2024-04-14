print("======= SEJA BEM VINDO A SUA CONTA ==========")
print("======== O QUE DESEJA FAZER HOJE?! ==========")

saldo = 0
limite = 500
extrato = ""
opcao = 0
quant_saques = 0
limite_saques = 3

while opcao != 4:

    print("""

[1] - Depósitar
[2] - Saque
[3] - Extrato
[4] - Sair

""")

    opcao = int(input("Selecione Uma Das Opçoes Acima: "))

    if opcao == 1:

        print("\nVoce Escolheu a Opção de Depósito!")

        deposito = float(input("\nOk!...Quanto deseja depositar?: "))

        print("\n")

        if deposito > 0:

            print(f"===== Seu depósito de: R${deposito: .2f}, foi realizado com sucesso!=====\n")

            saldo += deposito
            extrato += f"voce efetuou um deposito de:R${deposito: .2f}\n"

        else:
            print("===== A OPERAÇÂO FALHOU, TENTE NOVAMENTE! =====\n")        

    elif opcao == 2:

        print("\nEntendi, Você Gostaria de Sacar!\n")

        saque = float(input("\nQuanto Deseja Sacar?:"))

        if saque <= limite:

            print("===OPERAÇÃO REALIZADA COM SUCESSO! AGUARDE A CONTAGEM DAS CÉDULAS===\n")

        if saque > saldo:

            print("=====OPERACAO INVÁLIDA, SALDO INSUFICIENTE!=====\n")

        elif saque > limite:

            print("=====OPERACAO INVÁLIDA, LIMITE DE SAQUE EXCEDIDO!=====")

        elif quant_saques >= limite_saques:
        
            print("=====OPERACAO INVÁLIDA, LIMITE DE SAQUES DIARIOS EXCEDIDO!=====")

        elif saque > 0:

            saldo -= saque 
            extrato += f"Você realizou um saque de: R$ {saque:.2f} \n"
            quant_saques += 1
        

        else:

            print("=====OPERAÇAO INVÁLIDA, TENTE NOVAMENTE!=====")

    elif opcao == 3:

        print("\nOK... Vamos Ao Seu Extrato!\n")
        print("=================Extrato==================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")


    elif opcao == 4:
        print("\n==========SISTEMA FINALIZADO!===========")
        print("\n=============VOLTE SEMPRE!==============")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")




           
        





           








