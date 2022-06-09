number = ''

while not number.isdigit():
    number = input('Введіть кількість зірок: ')
    print(number)

print('*' * int(number))
