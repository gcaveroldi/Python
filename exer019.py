from math import radians, cos, sin, tan
ang = float(input('Digite o angulo a ser cálculado: '))
cos = cos(radians(ang))
sin = sin(radians(ang))
tan = tan(radians(ang))
print('O valor do Cosseno do angulo é: {:.2f}\n'
      'O valor do Seno do angulo é: {:.2f}\n'
      'O Valor da Tangente do angulo é: {:.2f}'.format(cos, sin, tan))


