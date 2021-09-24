# sequencia fibonacci
def fibo_func():
    try:
        valor_anterior = 0
        valor_posterior = 1
        soma = 1
        valor_max = int(input("Entre com o valor máx da sequencia: "))
        for soma in range(valor_max):
            print(valor_anterior)
            soma = valor_posterior + valor_anterior
            valor_anterior = valor_posterior
            valor_posterior = soma
    except ValueError:
        print("Fomato invalido!")


def opcao_fibo():
    opcao_continuar = "sim"
    opcao_fonecedida = input("Deseja imprimir sequencia?")
    while(opcao_fonecedida != "não"):
        if opcao_fonecedida != opcao_continuar:
            opcao_fonecedida = input("Tente novamente: ")
        else:
            fibo_func()
            opcao_fonecedida = input("Deseje continuar? ")

    print("Processo encerrando!")


opcao_fibo()
