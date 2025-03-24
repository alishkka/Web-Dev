# Task 1: Нахождение наибольшего из двух чисел
a = int(input())
b = int(input())
print(max(a, b))

# Task 2: Проверка на високосный год
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

# Task 3: Проверка симметричности числа
system_answer = int(input())
student_answer = int(input())
if system_answer == student_answer:
    print("YES")
else:
    print("NO")

# Task 4: Функция sign(x)
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

# Task 5: Сравнение двух чисел
a = int(input())
b = int(input())
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)