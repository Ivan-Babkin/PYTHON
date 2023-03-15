'''
Задача 6
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

Пример:
385916 -> yes
123456 -> no
'''
import os
os.system('cls')

while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print(f' ')
            print('ЗДОРОВО!!! Ваш билет СЧАСТИВЫЙ и Вы ДОЛЖНЫ его СЪЕСТЬ!')
            print(f' ')
        else:
            print(f' ')
            print('ОЧЕНЬ ЖАЛЬ, Ваш билет НЕ счастливый, но Вы можете купить еще один билет на удачу ;-)')
            print(f' ')
        break
    else:
        print(f' ')
        print('ЧТО Вы ввели? Это некорректный номер билета, попробуйте еще раз ...)')
        print(f' ')