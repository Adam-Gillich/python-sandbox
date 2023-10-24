# To clear the console:
# os.system('cls' if os.name == 'nt' else 'clear')
# os.system('cls||clear')

import time
from termcolor import cprint


def input_integer(text):
    while True:
        try:
            value = int(input(text).strip())
        except ValueError:
            cprint('\nYou can only use whole numbers!\n', color='red', force_color=True)
            continue
        return value


time_ = input_integer('What time do you want to count down from?\nPlease Enter seconds: ')
print()

for i in range(time_, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 24
    print(f'\r{hours}:{minutes: 03}:{seconds: 03}', end='')
    time.sleep(1)
print('\rProcess finished!')
input('\nPres Enter to finish! ')
