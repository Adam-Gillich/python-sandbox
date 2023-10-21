#video inspiration: https://www.youtube.com/watch?v=ssDBqQ5f5_0&pp=ygUcd2h5IGRpdmlzaW9uIHN1Y2tzIGluIGNvZGluZw%3D%3D
from termcolor import cprint


def c_convert_to_f(c):
    convert_to_f = c * (9 / 5) + 32
    convert_to_f = round(convert_to_f, 2)
    print(f'{c} °C converted to Fahrenheit is: {convert_to_f} °F')


def f_convert_to_c(f):
    convert_to_c = (f - 32) * 5 / 9
    convert_to_c = round(convert_to_c, 2)
    print(f'{f} °F converted to Celsius is: {convert_to_c} °C')


def lorem_ipsum(unit):
    while True:
        try:
            value = float(input(f'\nWhat {unit} value do you want to convert: ').replace(',', '.'))
        except ValueError:
            cprint('\nYou can only use numbers.', color='red', force_color=True)
            continue
        return value


def decide():
    while True:
        d = input('Which method do you want to use?\nCelsius to Fahrenheit (c)\nFahrenheit to Celsius (f)\n').strip()
        if d == "c":
            c_convert_to_f(lorem_ipsum('°C'))
            break
        elif d == "f":
            f_convert_to_c(lorem_ipsum('°F'))
            break
        else:
            cprint('You can only answer c or f.\n', color='red', force_color=True)


decide()

input('\nPress Enter to finish.')
