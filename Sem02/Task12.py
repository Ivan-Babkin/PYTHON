'''
Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''

import os
os.system('cls')

s = int(input('Введите сумму числе "S": '))
p = int(input('Введите произведение "P": '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(' ')
            print(f'Первое натуральное число будет: {x}')
            print(f'Второе натуральное число будет: {y}')
            print(' ')

# или

'''for x in range(s):
    y = s - x
    if x + y == s and x * y == p:
        a += 1
        print(x, y)
        break'''
if a == 0:
    print(' ')
    print('ОЙ - Вы ввели не корректные данные!')
    print(' ')