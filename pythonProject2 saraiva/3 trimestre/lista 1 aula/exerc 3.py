def resultadoSoma(n,n1):
    return print(f'A soma dos números é: {n + n1}')

def resultadoSubtracao(n,n1):
    return print(f'A subtração dos números é: {n - n1}')

def resultadoMultiplicacao(n,n1):
    return print(f'A multiplicação dos números é: {n * n1}')

def resultadoDivisao(n,n1):
    return print(f'A divisão dos números é: {n / n1}')

n = int(input("Digite um número inteiro: "))
n1 = int(input("Digite outro número inteiro: "))

resultadoSoma(n,n1)
resultadoSubtracao(n,n1)
resultadoMultiplicacao(n,n1)
resultadoDivisao(n,n1)