def resultadoTabuada(n, tabuada):
    while tabuada <= 10:
        print(f' {n} x {tabuada} = {n * tabuada}')
        tabuada += 1

n = int(input("Digite um número inteiro: "))
tabuada = 1
resultadoTabuada(n, tabuada)