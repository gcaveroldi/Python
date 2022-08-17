print('DESCUBRA QUANTO DE TINTA IRÁ GASTAR')
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede:  '))
a1 = l*a
tinta = a1/2
print('Você tem {:.2f}m² de parede. \nAssim precisará de {:.2f} l de tinta para pintar esta parede.'.format(a1,tinta))
