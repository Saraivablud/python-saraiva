def resultadoFinal(nSomados, valor):
    return print(f"Somando todos os valores e subtraindo por 10 o resultado é {nSomados - valor}")


n = int(input('Digite um número inteiro: '))
n1 = int(input('Digite outro número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
n3 = int(input('Digite o último número inteiro: '))
nSomados = (n + n1 + n2 + n3)
valor = 10

resultadoFinal(nSomados, valor)