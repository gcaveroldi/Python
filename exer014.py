salário = float(input('Digite o Valor do Salário para Reajuste: R$ '))
reajuste = (salário * 15 / 100 + salário)
print('O valor do Salário reajustado em 15% é R$ {:.2f}'.format(reajuste))
