# Task 1: Вывод всех четных чисел от a до b
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

# Task 2: Числа на отрезке от a до b, дающие остаток c при делении на d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")

# Task 3: Полные квадраты на отрезке от a до b
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if int(i**0.5)**2 == i:
        print(i, end=" ")

# Task 4: Наименьший делитель числа x, отличный от 1
x = int(input())
for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

# Task 5: Все делители числа x
x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")

# Task 6: Количество делителей числа x
x = int(input())
count = 0
for i in range(1, x + 1):
    if x % i == 0:
        count += 1
print(count)

# Task 7: Сумма 100 чисел
total = 0
for _ in range(100):
    total += int(input())
print(total)

# Task 8: Подсчет количества нулей среди N чисел
n = int(input())
zero_count = 0
for _ in range(n):
    if int(input()) == 0:
        zero_count += 1
print(zero_count)


#While Loop

# Task 1: Все точные квадраты натуральных чисел, не превосходящие N
N = int(input())
i = 1
while i * i <= N:
    print(i * i)
    i += 1

# Task 2: Наименьший натуральный делитель числа N, отличный от 1
N = int(input())
for i in range(2, N + 1):
    if N % i == 0:
        print(i)
        break

# Task 3: Все целые степени двойки, не превосходящие N
N = int(input())
power = 1
while power <= N:
    print(power, end=" ")
    power *= 2

# Task 4: Проверка, является ли число N точной степенью двойки
N = int(input())
power = 1
while power < N:
    power *= 2
if power == N:
    print("YES")
else:
    print("NO")

# Task 5: Наименьшее целое число k, такое что 2^k ≥ N
N = int(input())
k = 0
power = 1
while power < N:
    power *= 2
    k += 1
print(k)