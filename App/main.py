from input import *
from calc import *

# Run:
#   python App/main.py

def main():
    # Input parameters
    a = input_a()
    b = input_b()
    c = input_c()

    # Do the business logic 
    xx = solve_2nd_eq(a, b, c)
    
    # Print result
    print('Megoldások:', xx)
    
    # Wait for end
    input('\nNyomj Enter-t a program befejezéséhez.')

if __name__ == "__main__":
    main()
