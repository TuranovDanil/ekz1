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


# 24
