import math
from termcolor import cprint


def lorem_ipsum(text):
    while True:
        try:
            value = float(input(text).replace(',', '.').strip())
        except ValueError:
            cprint('Csak számokat írhatsz be!', color='red', force_color=True)
            continue
        return value


while True:
    a = lorem_ipsum('Add meg a másodfokú tagot: ')
    if a == 0:
        cprint('A másodfokú tag nem lehet 0!', color='red', force_color=True)
    else:
        break

b = lorem_ipsum('Add meg az elsőfokú tagot: ')
c = lorem_ipsum('Add meg a számot: ')


d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Nincs megoldás mert, d =', d)
elif d > 0:
    print('X1 =', (-b + math.sqrt(d)) / (2 * a), '\nX2 =', (-b - math.sqrt(d)) / (2 * a))
elif d == 0:
    print('Mivel d = 0, ezért csak egy megoldás van:', -b / (2 * a))

input('\nNyomj Enter-t a program befejezéséhez.')
