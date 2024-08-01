#Condicionales simples
'''temperature = 30

if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')'''

#condicionales anidadas

'''temperature = 40

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')'''

#ASIGNACION DE CONDICIONALES

'''temperature = 20

fire_risk = 'LOW' if temperature < 30 else 'HIGH'

print(fire_risk)'''

#MATCH-CASE



'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''

radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)