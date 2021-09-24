# cálculos de matemática básica e tratamento de erros
# cálculo de apenas 2 valores

def calculo_divisao():
    num_dividendo = int(input("Entre com o valor do dividendo: "))
    num_divisor = int(input("Entre com o valor do divisor: "))
    calculo_div = num_dividendo / num_divisor
    print("Resultado da divisão: ", calculo_div)


def calculo_multiplicacao():
    primeiro_fator = int(
        input("Entre com o primeiro fator para a multplicação: "))
    segundo_fator = int(
        input("Entre com o segundo fator para a multiplicação: "))
    calculo_mult = primeiro_fator * segundo_fator
    print("Resultado (produto) da multiplicação: ", calculo_mult)


def calculo_adicao():
    primeiro_valor_soma = int(
        input("Entre com o primeiro valor para adição: "))
    segundo_valor_soma = int(input("Entre com o segundo valor da adição: "))
    calculo_adicao = primeiro_valor_soma + segundo_valor_soma
    print("Resultado da adição: ", calculo_adicao)


def calculo_subtracao():
    primeiro_valor_minuendo = int(
        input("Entre com o primeiro valor para subtrair: "))
    segundo_valor_subtraendo = int(
        input("Entre com o segundo valor para subtrair: "))
    calculo_subtracao = primeiro_valor_minuendo - segundo_valor_subtraendo
    print("Resultado (diferença) da subtração: ", calculo_subtracao)


calculo_divisao()
calculo_multiplicacao()
calculo_adicao()
calculo_subtracao()
