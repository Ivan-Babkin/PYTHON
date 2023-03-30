'''
Задача 26
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''

import os
os.system('cls')

def recApowB(a, b):
    if b == 0:
        return 1
    return a * recApowB(a, b - 1)

a = int(input('Введите число "A": '))
b = int(input('Введите степень "B": '))
print(recApowB(a, b))
print(' ')