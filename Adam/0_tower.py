height = 12

a = 0
def single_0_tower(a):
    for i in range(height):
        a += 1
        print(a * '0')

        if a == height:
            break

print('\nSingle tower\n')
single_0_tower(a)
print('\n\n')


c = 12
def inverted_0_tower(x, y):
    for i in range(height):
        x -= 1
        y += 1
        print(x * ' ', y * '0')

print('Inverted\n')
inverted_0_tower(c, y=0)
print('\n\n')


d = 0
x1 = height
def triangle_0_tower(a , x, y):
    for i in range(height):
        a += 1
        x -= 1
        y += 1
        print(x * ' ', y * '0', a * '0', sep= '')

print('Triangle tower\n')
triangle_0_tower(d, x1, y=0)
print('\n\n')


times = 2
b = 0
def wave_of_0s(b, times):
    while times > 0:
        for i in range(height):
            b += 1
            if height == 0:
                break
            print(b * '0')
            
        for x in range(height):
            b -= 1
            print(b * '0')
        times -= 1

print('Wave\n')
wave_of_0s(b, times)
print('\n\n')


input('\nPress Enter to finish')