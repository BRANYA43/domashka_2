digit = ''

while not digit.isdigit():
    digit = input('Будь ласка введіть ціле число: ')

digit = int(digit)
print(f'Наступне число пілся {digit} є {digit + 1}\n'
      f'Попередне число перед {digit} є {digit - 1}')
