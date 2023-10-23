# To clear the console:
# os.system('cls' if os.name == 'nt' else 'clear')
# os.system('cls||clear')

import time

time_ = int(input('What time do you want to count down from? '))

for i in range(time_, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 24
    print(f'\r{hours}:{minutes: 03}:{seconds: 03}', end='')
    time.sleep(1)
