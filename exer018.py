from math import hypot
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hipo = hypot(co, ca)
print('A medida da Hipotenusa deste Triangulo Retangulo é:  {:.2f}'.format(hipo))
