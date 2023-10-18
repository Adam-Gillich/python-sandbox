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

def input_a():
    while True:
        a_str = str(input('Add meg a másodfokú tagot: ')).replace(',', '.')

        a = tryfloat(a_str)

        if isinstance(a, (int, float)) and a != 0:
            break
        error_messages(a)
    
    return a

def input_b():
    while True:
        b_str = str(input('Add meg az elsőfokú tagot: ')).replace(',', '.')

        b = tryfloat(b_str)

        if isinstance(b, (int, float)):
            break
        print('Csak számokat írhatsz be!')
    
    return b
    
def input_c():    
    while True:
        c_str = str(input('Add meg a számot: ')).replace(',', '.')

        c = tryfloat(c_str)

        if isinstance(c, (int, float)):
            break
        print('Csak számokat írhatsz be!')
    
    return c
