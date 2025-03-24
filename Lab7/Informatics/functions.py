# Function to find the minimum of four numbers
def min_of_four(a, b, c, d):
    return min(a, b, c, d)

# Function to calculate a^n
def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Function to implement XOR operation
def xor(x, y):
    return (x and not y) or (not x and y)

# Main part of the program
if __name__ == "__main__":
    # Task 1: Minimum of four numbers
    a, b, c, d = map(int, input().split())
    print(min_of_four(a, b, c, d))

    # Task 2: Power calculation
    a = float(input())
    n = int(input())
    print(power(a, n))

    # Task 3: XOR operation
    x, y = map(int, input().split())
    print(int(xor(bool(x), bool(y))))