dict1 = {"first": 1, "second": 2, "third": 3}

for keys, value in dict1.items():
print(keys, value)
print(dict1.items())

# Кортежи

print(dict1)
dict1.update({"four": 4, "five": 5})
print(dict1)
#
print(dict1["second"])
#
print(dict1.get("second"))
print(dict1.get("four", 0)) #если значения нет, то пусть выводит 0 вместо none
print(dict1)
dict1.pop("second")  #убирает из выдачи то значение, которое указали
print(dict1)
print(dict1.keys()) #Возвращает название
print(dict1.values()) #Возвращает значение
#
dict1 = {'Tom': {'English': 5, "Math": 5}, 'Red': {'English': 4, "Math": 4}}

print(dict1)
for i in dict1['Tom'].items():
    print(*i)
print()
print(dict1['Red']['Math'])

dict1.update({'Wer': {'English': 3, "Math": 3}}) #update добавляет информацию
print(dict1)

dict1['Tom'].update({'Trud': 6}) #update добавляет информацию из словаря именно по Тому
print(dict1)
dict1['Red']['Math'] = 5 #Добавление новой информации вместо старой, т.е. Ред исправил математику с 4 на 5
print(dict1)

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию
n = int(input('Введите значение: '))
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
fib(n)
print(list_1[n])

# #2 решение

def f(n):
    if n == 0 or n == 1:
        return n
    return f(n - 1) + f(n - 2)

print(f(int(input())))
# 33.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

n = int(input('Введите количество оценок:  '))
list1 = [int(input('Введите оценки:')) for i in range(n)]
print(list1)

maxM = 0
minM = list1[0]
for i in list1:
    if i>maxM:
        maxM=i
    if i<minM:
        minM=i
for i in range(len(list1)):
    if list1[i]==maxM:
        list1[i]=minM
print(list1)
# # 2 решение
list1 = [int(i) for i in input('Введите оценки: ').split()]
max_n = max(list1)
min_n = min(list1)
list1 = [min_n if list1[i] == max_n else list1[i] for i in range(len(list1))]
print(list1)

#3 решение

n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
print(list1)
# list1 = [int(input()) for i in range(int(input()))]

max_n = max(list1)
min_n = min(list1)

for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n

print(list1)
# 35.Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes
def prime(n):
    i = 2
    flag = True
    while i < n // 2 + 1 and flag:
        if n % i == 0:
            flag = False
            i += 1
        if flag:
            return "yes"
        return "no"
print(prime(int(input())))
# 37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f'{k}'
print(f(int(input())))


