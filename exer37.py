casa = float(input('Valor da casa: '))
salário = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo Negado!')
