# Task 1: Print "Hello, World!"
print("Hello, World!")

# Task 2: Conditional actions based on an integer
def check_weird(n):
    if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")

# Task 3: Sum, difference, and product of two integers
def arithmetic_operations(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

# Task 4: Integer and float division
def division_operations(a, b):
    print(a // b)
    print(a / b)

# Task 5: Print squares of non-negative integers less than n
def print_squares(n):
    for i in range(n):
        print(i ** 2)

# Task 6: Check if a year is a leap year
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Task 7: Print integers from 1 to n as a single string
def print_consecutive_integers(n):
    print("".join(map(str, range(1, n + 1))))

# Task 8: List comprehensions for 3D grid
def list_comprehensions(x, y, z, n):
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

# Task 9: Find the runner-up score
def runner_up_score(arr):
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    print(unique_scores[1])

# Task 10: Find students with the second lowest grade
def second_lowest_grade(students):
    grades = sorted(set([grade for name, grade in students]))
    second_lowest = grades[1]
    names = sorted([name for name, grade in students if grade == second_lowest])
    for name in names:
        print(name)