populacaoMundial = float(input("digite o numero da populsço mundial "))
crescimentoPopulacional = float(input("digite a taxa (%) "))  / 100
ano = int(input("Digite o número de anos para estimar o crescimento: "))
populacaoFutura = populacaoMundial * (1 + crescimentoPopulacional) * ano




print("A população estimada após {ano} ano(s) será de:", {populacaoFutura})
