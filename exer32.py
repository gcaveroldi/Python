distância = float(input('Qual adistância dasua viagem: '))
print('Você está prestes a comerçar uma viagem de {}km.')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
