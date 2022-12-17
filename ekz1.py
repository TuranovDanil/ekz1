

# # 1
# numbers = int(input('Введите число: '))
# positive = 0
# negative = 0
# while numbers != -65432:
#     if numbers >= 0:
#         positive += 1
#     else:
#         negative += 1
#     numbers = int(input('Введите число: '))
# _sum = negative + positive
# print('Процент положительных чисел: ', round(positive / _sum, 2) * 100, '%',
#       '\nПроцент отрицательных чисел: ', round(negative / _sum, 2) * 100, '%')
#
# # 2
# sum = 0  # Сумма
# countTerms = 0  # Количество слагаемых
#
# while True:
#     num = int(input())
#
#     if num < 0:
#         break
#
#     if num % 2 != 0:
#         sum += -num
#     else:
#         sum += num * num
#
#     countTerms += 1
#
# print(f'Сумма = {sum}')
# print(f'Количество слагаемых = {countTerms}')
#
# # 3
#
# arr = []
# M = 3
#
# for i in range(0, M):
#     arr.append(input().replace('?', '*'))
#
# print(arr)
#
# # 4
# M = int(input('Введите положительное число: '))
# while M <= 0:
#     M = int(input('Введите положительное число: '))
#
# empt = list()
# k = 0
#
# while k != M:
#     a = input('Введите строчку: ')
#     empt.append(a.count(' '))
#     k += 1
#
# k = 1
# for elem in empt:
#     print('В строке: ' + str(k) + ', количество пробелов: ' + str(elem))
#     k += 1
#
# # 5
# print('''Вводите текст, отделяя строки
# нажатием Enter, последней строкой
# введите слово Конец''')
# while True:
#     s = str(input())
#     if (s == 'Конец' or s == 'конец'):
#         break
#     k = 0
#     for x in s:
#         if x in 'ёуеыаоэяиюЁУЕЫАОЭЯИЮ':
#             k += 1
#     print(k)
#
# # 6
# M = 3
# chars = []
#
# for i in range(M):
#     chars.append(input())
#
# word = ' '.join(chars)
#
# print(word)
#
# # 7 работает с числами, символами и инглиш буквами, но не с буквами русскими
# M = 3
# arr = []
#
# for i in range(M):
#     arr.append(input())
#
# maximux = len(max(arr))
#
# for i in range(len(arr)):
#     cem = maximux - len(arr[i])
#     print('*' * cem + str(arr[i]))
#
# # 8
# a = [1, 2, 3, 4, 5]
# b, c = map(int, input().split())
# for i in a[b:c]:
#     a.remove(i)
# print(a)


# 1
# numbers = int(input('Введите число: '))
# positive = 0
# negative = 0
# while numbers != -65432:
#     if numbers >= 0:
#         positive += 1
#     else:
#         negative += 1
#     numbers = int(input('Введите число: '))
# _sum = negative + positive
# print('Процент положительных чисел: ', round(positive / _sum, 2) * 100, '%',
#       '\nПроцент отрицательных чисел: ', round(negative / _sum, 2) * 100, '%')

# # 2
# sum = 0
# sumCount = 0
#
# while True:
#     num = int(input())
#
#     if num < 0:
#         break
#
#     if num % 2 != 0:
#         sum += -num
#     else:
#         sum += num * num
#
#     sumCount += 1
#
# print('Сумма = ', sum)
# print('Кол-во слагаемых = ', sumCount)

# 3
# arr = []
# M = 3
#
# for i in range(0, M):
#     arr.append(input().replace('?', '*'))
#
# print(arr)

# 4
# M = int(input('Сколько строк: '))
#
# for i in range(M):
#     stri = input('Введите ' + str(i + 1) + ' строку: ')
#     # K - число пробелов
#     spaces = stri.count(' ')
#     print('В', i + 1, 'строке', spaces, 'проб.')

# 5
# while True:
#     s = str(input('Введите строку\n'))
#     if (s == 'Выход' or s == 'выход'):
#         break
#     glasnaya = 0
#     for x in s:
#         if x in 'ёуеыаоэяиюЁУЕЫАОЭЯИЮ':
#             glasnaya += 1
#     print(glasnaya)

# 6
# print(' '.join([input() for i in range(int(input('M = ')))]))

# M = random.randint(1, 5)
# arr = [random.randint(1, 5) for i in range(M)]
#
# for i in range(M):
#     arr[i] = input()
# print(arr)
# b = arr[0]
#
# for i in range(1, M):
#     b = str(b) + " " + arr[i]
# print(b)

# 7
# M = int(input('Число строк: '))
# arr = []
#
# for i in range(M):
#     arr.append(input('Введите строку: '))
# arr.sort()
# arr.reverse()
# print(f'Самая длинная строка - {arr[0]} = {len(arr[0])} символов')
#
# for i in range(len(arr)):
#     print('*' * len(arr[i]) + arr[i])



# 14
# A = int(input('Введите год: '))
#
# if (((A % 4 == 0) and (A % 100 != 0)) or (A & 400 == 0)):
#     print(A, "високосный год")
#     print(((A - 1) // 100) + 1, 'век')
#
# elif ((A % 4 != 0) or ((A % 100 == 0) and (A & 400 != 0))):
#     print(A, "не високосный год")
#     print(((A - 1) // 100) + 1, 'век')

# 15
# print('Стороны треугольника')
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a + b > c and a - b < c:
#     print("существует")
# else:
#     print("не существует")
# if c ** 2 == a ** 2 + b ** 2:
#     print("прямоугольный")
# else:
#     print("не прямоугольный")

# 16
# import math
#
# M = int(input('объем жидкости M = '))
# A = int(input('кубическая емкость A = '))
# R = int(input('R основания = '))
# H = int(input('цилиндрическая с высотой H = '))
#
# if M <= A ** 3 and M <= math.pi * R ** 2 * H:
#     print('Жидкость поместится в оба')
# elif M <= A ** 3:
#     print('Жидкость поместится в первом')
# elif M <= math.pi * R ** 2 * H:
#     print('Жидкость поместится в первом')
# else:
#     print('Не поместиться ни в одном')

# 17
# A = int(input('Сторона коробки А = '))
# B = int(input('Сторона коробки В = '))
# C = int(input('Сторона коробки С = '))
# M = int(input('Размер двери М = '))
# K = int(input('Размер двери К = '))
# if (A < M and B < K) or (A < K and B < M):
#     print("помещается")
# elif (B < M and C < K) or (B < K and C < M):
#     print("помещается")
# elif (A < M and C < K) or (A < K and C < M):
#     print("помещается")
# else:
#     print("не помещается")

# 18.1
# import random
#
# X = random.randint(1, 54)
# print(X)
# if X > 40:
#     print("боковое")
# else:
#     print("купе")
# if X % 2 == 0:
#     print("верхнее")
# else:
#     print("нижнее")

# 18.2
# n = int(input('Введите номер вашего места в плацкартном вагоне: '))
# print()
# if n > 36:
#     print('Ваше место - боковое.')
# elif n % 2:
#     print('Ваше место в купе внизу.')
# else:
#     print('Ваше место в купе наверху.')

# 19
# import random
#
# M = random.randint(1, 5000)
# print("Всего денег = " + str(M))
#
# A = M % 500
# A1 = M // 500
# print("500: " + str(A1))
#
# B = A % 100
# B1 = A // 100
# print("100:" + str(B1))
#
# C = B % 10
# C1 = B // 10
# print("10:" + str(C1))
#
# D1 = C // 2
# print("2:" + str(D1))

# 20 эта задача вроде тоже самое что и 16ая но хз
# import math
#
# M = int(input('объем жидкости M = '))
# A = int(input('кубическая емкость A = '))
# R = int(input('R основания = '))
# H = int(input('цилиндрическая с высотой H = '))
#
# if M <= A ** 3 and M <= math.pi * R ** 2 * H:
#     print('Жидкость поместится в оба')
# elif M <= A ** 3:
#     print('Жидкость поместится в первом')
# elif M <= math.pi * R ** 2 * H:
#     print('Жидкость поместится в первом')
# else:
#     print('Не поместиться ни в одном')

# 21
# import random
#
# a = random.randint(1, 100)
# print("a= " + str(a))
#
# b = random.randint(1, 100)
# print("b= " + str(b))
#
# c = random.randint(1, 100)
# print("c= " + str(c))
#
# d = random.randint(1, 100)
# print("d= " + str(d))
#
# if (a <= c and b <= d) or (a <= d and b <= c):
#     print("Прямоугольник со сторонами a,b может поместиться в прямоугольник со сторонами c,d")
# else:
#     print("Прямоугольник со сторонами a,b не может поместиться в прямоугольник со сторонами c,d")

# 22
# N = int(input('Количество элементов массива = '))
# arr = [int(input('Введите элемент массива: ')) for i in range(N)]
# M = int(input('Количество исключаемых элементов '))
# K = int(input('Номер элемента массива '))
#
# arr[K:K+M] = []
# print('Итог ', arr)

# 23
# N = int(input('Длина массива: '))
# numbers = [int(input('Введите элемент массива: ')) for i in range(N)]
# new_numbers = []
# for i in range(len(numbers)):
#     if numbers[i] != 0:
#         new_numbers.append(numbers[i])
#
# print('Итоговый массив - ', new_numbers)

# 24
# N = int(input('Длина массива: '))
# numbers = [int(input('Введите элемент массива: ')) for i in range(N)]
# for i in range(len(numbers)):
#     if numbers[i] == 0:
#         numbers[i] = numbers[i - 1] + numbers[i - 2]
#
# print('Итоговый массив - ', numbers)

# 25
# N = int(input('Длина массива: '))
# numbers = [float(input('Введите элемент массива: ')) for i in range(N)]
# divisionBy3 = 0  # количество чисел делящихся на 3
# even = []  # список четных чисел
# for n in numbers:
#     if n % 3 == 0:
#         divisionBy3 += 1
#     elif n % 2 == 0:
#         even.append(n)
#
# m = sum(even) / len(even)
# numbers.insert(0, divisionBy3)
# numbers.append(m)
# print(numbers)


# 25
# import array as arr
# import random
# num = arr.array('i', [])
# while True:
#     try:
#         N = int(input('введите кол-во\n'))
#         break
#     except:
#         print('введено не чило')
#         continue
# i = 0
# while i < N:
#     num.append(random.randint(-100, 100))
#     i += 1
#
# print(num)
# counter = 0
# counterChet = 0
# sumChet = 0
# for item in num:
#     if item % 3 == 0:
#         counter += 1
#     elif item % 2 == 0:
#         counterChet += 1
#         sumChet += item
# print(f'кол-во дел на 3 {counter}')
# a = int(sumChet/counterChet)
# print(f'сред.ар. четных {a}')
# num.insert(0, counter)
# num.append(a)
# print(num)


# 26
# counterSum = 0
# sum = 0
# prod = 1
# counterProd = 0
# while True:
#     try:
#         buf = float(input('введите число \n'))
#     except:
#         print('введено не число')
#         continue
#     if buf == 55555:
#         print(f'\nсумма {sum} произведение {prod} кол-во слагаемых{counterSum} кол-во сомножителей{counterProd}\n')
#         break
#     elif buf % 2 == 0:
#         counterProd += 1
#         prod *= buf
#     else:
#         counterSum += 1
#         sum += buf

# 27
# sum = 0
# counter = 0
# prod = 1
# while True:
#     try:
#         P = float(input('введите P \n'))
#         H = float(input('введите H \n'))
#         break
#     except:
#         print('введено не число')
#         continue
# while True:
#     try:
#         buf = float(input('введите число \n'))
#     except:
#         print('введено не число')
#         continue
#     if buf == P or buf == H:
#         print(f'\nитоговая сумма {sum} итоговое произведение {prod} итоговое кол-во {counter}\n')
#         break
#     elif buf < P:
#         sum += buf
#     elif buf > H:
#         prod *= buf
#     elif buf <= P and buf >= H or buf <= H and buf >= P:
#         counter += 1


# 28
# counter = 0
# while True:
#     try:
#         buf = float(input('введите число \n0 вывод суммы\n99999 конец\n'))
#     except:
#         print('введено не число')
#         continue
#     if buf == 99999:
#         break
#     elif buf == 0:
#         print(f'\nсумма {counter}\n')
#     else:
#         counter += buf
#
# print(f'\nитоговая сумма {counter}\n')

# 29
# a = []
# b = 5
# conter = 0
# while True:
#     try:
#         buf = float(input('введите число положительное число, <0 закончить\n'))
#     except:
#         print('введено не число')
#         continue
#     if buf < 0:
#         print('конец')
#         break
#     else:
#         a.append(buf)
#         if buf % b == 0:
#             conter += 1
#
# print(a, conter)

# 30
# import array as arr
#
# num = arr.array('i', [])
# N = int(input('введите кол-во чисел\n'))
# i = 0
# while i < N:
#     buf = int(input('число\n'))
#     num.append(buf)
#     i += 1
#
# print(num)
# i = 0
# while i < N:
#     if num[i] == num[i - 1] == 0:
#         print('два нуля')
#         break
#     i += 1
# else:
#     print('нет такого')












