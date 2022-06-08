number = ''

while not number.isdigit():
    number = input('Введіть число кількості зірок: ')

print('*' * int(number))
