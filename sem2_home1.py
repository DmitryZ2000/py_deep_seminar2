# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


while True:
    num = input('Введите целое чило:   ')
    if num.isdigit():
        num = int(num)
        break

print(f'{num} is {hex(num)}')

my_hex = ''

while num:
    hex_digit = num % 16
    if hex_digit == 10:
        my_hex = 'A' + my_hex
    elif hex_digit == 11:
        my_hex = 'B' + my_hex
    elif hex_digit == 12:
        my_hex = 'C' + my_hex
    elif hex_digit == 13:
            my_hex =  'D' + my_hex
    elif hex_digit == 14:
        my_hex = 'E' + my_hex
    elif hex_digit == 15:
        my_hex = 'F' + my_hex
    else:
        my_hex = str(hex_digit) + my_hex
    num = num // 16

print('hex is ', my_hex)
