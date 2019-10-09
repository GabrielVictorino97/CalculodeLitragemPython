from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()
comodo = Comodo(input('Qual a largura do comodo? '), input('Qual profundidade do comodo? '))

print("A área da parede é: ", calc.calcular_area_parede
    (comodo))

print("A área do teto é", calc.calcular_area_teto
    (comodo))

print('A litragem de tinta necessária é: ', (calc.calcular_litragem_necessaria()))