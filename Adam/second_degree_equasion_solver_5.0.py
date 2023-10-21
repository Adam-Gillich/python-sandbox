import math
from termcolor import cprint


def tryfloat(i):
    try:
        return float(i)
    except ValueError:
        return i


while True:
    a_str = str(input('Add meg a másodfokú tagot: ')).replace(',', '.').strip()

    a = tryfloat(a_str)

    if isinstance(a, (int, float)) and a != 0:
        break
    if a == 0:
        cprint('A másodfokú tag nem lehet 0!', color='red', force_color=True)
    if a != 0:
        cprint('Csak számokat írhatsz be!', color='red', force_color=True)

while True:
    b_str = str(input('Add meg az elsőfokú tagot: ')).replace(',', '.').strip()

    b = tryfloat(b_str)

    if isinstance(b, (int, float)):
        break
    cprint('Csak számokat írhatsz be!', color='red', force_color=True)

while True:
    c_str = str(input('Add meg a számot: ')).replace(',', '.').strip()

    c = tryfloat(c_str)

    if isinstance(c, (int, float)):
        break
    cprint('Csak számokat írhatsz be!', color='red', force_color=True)

d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Nincs megoldás mert, d =', d)
elif d > 0:
    print('X1 =', (-b + math.sqrt(d)) / (2 * a), '\nX2 =', (-b - math.sqrt(d)) / (2 * a))
elif d == 0:
    print('Mivel d = 0, ezért csak egy megoldás van:', -b / (2 * a))

input('\nNyomj Enter-t a program befejezéséhez.')
