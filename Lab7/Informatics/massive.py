# Task 1: Elements with even indices
def even_indices_elements(arr):
    return arr[0::2]

# Task 2: Even elements
def even_elements(arr):
    return [x for x in arr if x % 2 == 0]

# Task 3: Count of positive elements
def count_positive_elements(arr):
    return sum(1 for x in arr if x > 0)

# Task 4: Count of elements greater than the previous one
def count_greater_than_previous(arr):
    return sum(1 for i in range(1, len(arr)) if arr[i] > arr[i - 1])

# Task 5: Check for adjacent elements with the same sign
def has_adjacent_same_sign(arr):
    for i in range(1, len(arr)):
        if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):
            return "YES"
    return "NO"

# Task 6: Count elements greater than both neighbors
def count_greater_than_neighbors(arr):
    return sum(1 for i in range(1, len(arr) - 1) if arr[i] > arr[i - 1] and arr[i] > arr[i + 1])

# Task 7: Reverse array in place
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr

# Main part of the program
if __name__ == "__main__":
    # Input for Task 1
    n = int(input())
    arr = list(map(int, input().split()))
    print(*even_indices_elements(arr))

    # Input for Task 2
    n = int(input())
    arr = list(map(int, input().split()))
    print(*even_elements(arr))

    # Input for Task 3
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_positive_elements(arr))

    # Input for Task 4
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_greater_than_previous(arr))

    # Input for Task 5
    n = int(input())
    arr = list(map(int, input().split()))
    print(has_adjacent_same_sign(arr))

    # Input for Task 6
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_greater_than_neighbors(arr))

    # Input for Task 7
    n = int(input())
    arr = list(map(int, input().split()))
    print(*reverse_array(arr))