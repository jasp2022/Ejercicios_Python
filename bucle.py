#WHILE

'''want_greet = 'S'  # importante dar un valor inicial

while want_greet == 'S':
    print('Hola qué tal!')
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''

#FOR

'''word = 'Python'

for letter in word:
    print(letter)'''

for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f'{num_table} * {mul_factor} = {result}')

