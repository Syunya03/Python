# Задача 18: Требуется найти в массиве Ai[1..Ai] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число Ai 
# – количество элементов в массиве. В последующих  строках записаны Ai целых чисел Aii.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     
#     -> 5

A = int(input('Длинна массива:'))
a = [int(input('Ввести число:')) for i in range(A)]
x = int(input('Заданное число:'))

min = (x - a[0])**2 

b = 0 
i = 0 
while i < len(a):
    if (x-a[i])**2 <= min:
        min = (x-a[i])**2
        b = i
        i += 1
print('Самое близкое значение элемента массива: ', a[b])



