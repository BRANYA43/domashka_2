number = ''

while not number.isdigit():
    number = input('Будь ласка введіть ціле число: ')

number = int(number)
print(f'Наступне число пілся {number} є {number + 1}\n'
      f'Попередне число перед {number} є {number - 1}')
