# Calculo de divisão com possibilidade de continuar calculando (sim/não)
# Função de controle no mesmo modulo
# Ainda não possui todas as validações no Menu Principal


def calculo_divisao_com_mais_numeros():
    global calculo_divisao

    try:
        valor1 = int(
            input("Insira um valor do tipo inteiro para o dividendo: "))

    except (ValueError, ZeroDivisionError):
        valor1 = False
        tentativas_max = 4
        for tentativas in range(tentativas_max):
            while valor1 == False:
                try:
                    valor1 = int(
                        input("Formato invalido! Tente novamente com um valor inteiro (dividendo): "))
                except ValueError:
                    if valor1 == ValueError:
                        valor1 = False
                    tentativas = tentativas + 1
                    print("Tentativa ", tentativas)

                if tentativas == tentativas_max:
                    print("Numero máximo de tentativas foi excedido!")
                break

    try:
        valor2 = int(
            input("Insira um valor do tipo inteiro para o divisor: "))
        while valor2 == 0:
            valor2 = int(input(
                "O valor do dividendo deve ser maior que ZERO! Insira um valor do tipo inteiro para o dividendo: "))

    except (ValueError, ZeroDivisionError):
        valor2 = False
        tentativas_max = 4
        for tentativas in range(tentativas_max):
            while valor2 == False:
                try:
                    valor2 = int(
                        input("Formato invalido! Tente novamente com um valor inteiro maior que ZERO(divisor): "))
                except (ValueError, ZeroDivisionError):
                    if valor2 == (ValueError, ZeroDivisionError):
                        valor2 = False
                    tentativas = tentativas + 1
                    print("Tentativa ", tentativas)

                if tentativas == tentativas_max:
                    print("Numero máximo de tentativas foi excedido!")
                break

    print("Valor 1 ok", valor1)
    print("Valor 2 ok", valor2)
    calculo_divisao = valor1 / valor2

    print("Resultado da operação: ", calculo_divisao)

    memoria_global_divisao = calculo_divisao

    memoria_dos_calculos()

    menu_principal()


def menu_principal():

    print("\nMenu Principal\n"
          "1 - Divisão\n"
          "2 - Multiplicação\n"
          "3 - Subtração\n"
          "4 - Adição\n"
          "0 - Sair\n")

    try:
        opcaoSelecionada = int(input("Insira uma opção para calculo: "))
        if opcaoSelecionada == 1:
            print("--- DIVISÃO ---")
            calculo_divisao_com_mais_numeros()
        elif opcaoSelecionada == 2:
            print("Opção multiplicação não está disponível!")
            menu_principal()
        elif opcaoSelecionada == 3:
            print("Opção de Subtração não está disponível!")
            menu_principal()
        elif opcaoSelecionada == 4:
            print("Opção de Adição não está disponível!")
            menu_principal()
        elif opcaoSelecionada == 0:
            print("Operação encerrada!")
            exit
        else:
            opcaoSelecionada = False

            while opcaoSelecionada == False:
                menu_principal()
                opcaoSelecionada = int(
                    input("Opção invalida! Insira uma das opções do Menu Principal: "))

    except Exception as erro:
        print("Erro identificado: ", {erro.__class__})


def memoria_dos_calculos():

    if calculo_divisao == 0:
        print("Ainda não existe valores em DIVISÃO!")
    else:
        print("Memória de cálculo de divisão: ", calculo_divisao)


menu_principal()
