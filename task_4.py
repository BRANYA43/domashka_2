from random import randint

for i in range(100):
    year = randint(0, 9999)

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year}р є високосним.')
    else:
        print(f'{year}р не є високосним.')
