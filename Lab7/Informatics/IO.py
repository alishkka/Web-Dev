#Task 1
import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

hypotenuse = math.sqrt(a**2 + b**2)

print(hypotenuse)
2

#Task 2
n = int(input())

print("The next number for the number", n, "is", n + 1, ".", sep=" ")
print("The previous number for the number", n, "is", n - 1, ".", sep=" ")

#Task 3
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

apples_per_student = K // N

print(apples_per_student)

# Task 4
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

apples_left_in_basket = K % N

print(apples_left_in_basket)

# Task 5
v = int(input("Enter the speed of the biker (v): "))
t = int(input("Enter the time of travel (t): "))

# Длина МКАД
mkad_length = 109

# Вычисление конечной отметки
final_position = (v * t) % mkad_length

# Приведение к положительному значению, если результат отрицательный
final_position = final_position if final_position >= 0 else mkad_length + final_position

# Вывод результата
print(final_position)