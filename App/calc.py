import math

def solve_2nd_eq(a, b, c):
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        print('Nincs megoldás mert, d =', d)
        return []
    elif d > 0:
        return [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
    elif d == 0:
        print('Mivel d = 0, ezért csak egy megoldás van')
        return [-b / (2 * a)]
