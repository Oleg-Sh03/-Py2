#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
#не превосходящие числа N.
#Пример:
#Ввод: 13 -> 1, 2, 4, 8
#После загрузки задания, вы можете проверить себя самостоятельно с помощью 
#эталонного решения

print("Введите положительное число N: ")
N = float(input())
if N >= 1:
    i = 0
    while 2**i <= N / 2:
        print(2**i, end=', ')
        i += 1
    print(2**(i))
else:
    print("Ошибка ввода")
