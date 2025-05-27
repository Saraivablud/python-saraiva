precodeCapaLivro = 24.95
precodeCapaLivroDesconto = precodeCapaLivro -(precodeCapaLivro * 0.40)
custoFretePrimeiroExemplar = precodeCapaLivroDesconto + 3.00
custoFreteRestanteExemplares = precodeCapaLivroDesconto + 0.75
custoTotalAtacado = custoFretePrimeiroExemplar +(custoFreteRestanteExemplares * 59)

print ("O custo total de atacado para 60 exemplares é de: ", custoTotalAtacado)