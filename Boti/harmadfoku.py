import sympy

print("A harmadfokú egyenlet formátuma: ax^3 + bx^3 + cx + d = 0")
a = float(input("Add meg az 'a' értékét: "))
b = float(input("Add meg az 'b' értékét: "))
c = float(input("Add meg az 'c' értékét: "))
d = float(input("Add meg az 'd' értékét: "))
x = sympy.symbols('x')

equation = sympy.Eq(a * x**3 + b * x**2 + c * x + d, 0)
solutions = sympy.solve(equation, x)
print("A harmadfokú egyenlet gyökei: ")
for sol in solutions:
    print(sol)
    
input("Nyomj enter a program befejezéséhez")