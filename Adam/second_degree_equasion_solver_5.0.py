import math


def tryfloat(i):
    try:
        return float(i)
    except ValueError:
        return i


def error_messages(i):
    if i == 0:
        print('A másodfokú tag nem lehet 0!')
    if i != 0:
        print('Csak számokat írhatsz be!')


while True:
    a_str = str(input('Add meg a másodfokú tagot: ')).replace(',', '.')

    a = tryfloat(a_str)

    if isinstance(a, (int, float)) and a != 0:
        break
    error_messages(a)

while True:
    b_str = str(input('Add meg az elsőfokú tagot: ')).replace(',', '.')

    b = tryfloat(b_str)

    if isinstance(b, (int, float)):
        break
    print('Csak számokat írhatsz be!')

while True:
    c_str = str(input('Add meg a számot: ')).replace(',', '.')

    c = tryfloat(c_str)

    if isinstance(c, (int, float)):
        break
    print('Csak számokat írhatsz be!')

d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Nincs megoldás mert, d =', d)
elif d > 0:
    print('X1 =', (-b + math.sqrt(d)) / (2 * a), '\nX2 =', (-b - math.sqrt(d)) / (2 * a))
elif d == 0:
    print('Mivel d = 0, ezért csak egy megoldás van:', -b / (2 * a))

input('\nNyomj Enter-t a program befejezéséhez.')
