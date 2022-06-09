year = ''

while not year.isdigit():
    number = input('Введіть рік: ')

year = int(year)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year}р є високосним.')
else:
    print(f'{year}р не є високосним.')
