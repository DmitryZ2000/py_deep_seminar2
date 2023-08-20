# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions as fr

f1 = input('Ввведите строкутроку вида “a/b” — дробь с числителем и знаменателем:  ')
f2 = input('Ввведите строкутроку вида “a/b” — дробь с числителем и знаменателем:  ')

# f1 = '1/7'
# f2 = '1/9'

f1_numerator = int(f1.split('/')[0])
f1_denominator = int(f1.split('/')[1])
f2_numerator = int(f2.split('/')[0])
f2_denominator = int(f2.split('/')[1])
print(f'{f1_numerator}/{f1_denominator} {f2_numerator}/{f2_denominator}')

sum_numerator = f1_numerator * f2_denominator + f2_numerator * f1_denominator
sum_denominator = f1_denominator * f2_denominator
print(f'Результат сложения: {sum_numerator} / {sum_denominator}')
print('Результат сложения контроль', fr.Fraction(f1_numerator, f1_denominator) \
       + fr.Fraction(f2_numerator, f2_denominator))

mult_numerator = f1_numerator * f2_numerator
mult_denominator = f1_denominator * f2_denominator
print(f'Результат произведения: {mult_numerator} / {mult_denominator}')
print('Результат произведения контроль: ', fr.Fraction(f1_numerator, f1_denominator) \
       * fr.Fraction(f2_numerator, f2_denominator))
