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
a = []
b = 5
conter = 0
while True:
    try:
        buf = float(input('введите число положительное число, <0 закончить\n'))
    except:
        print('введено не число')
        continue
    if buf < 0:
        print('конец')
        break
    else:
        a.append(buf)
        if buf % b == 0:
            conter += 1

print(a, conter)

