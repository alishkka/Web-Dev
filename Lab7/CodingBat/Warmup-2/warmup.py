# Function 1: Return a larger string that is n copies of the original string
def string_times(string, n):
    return string * n

# Function 2: Return n copies of the front (first 3 chars or less) of the string
def front_times(string, n):
    front = string[:3]
    return front * n

# Function 3: Return a new string made of every other char starting with the first
def string_bits(string):
    return string[::2]

# Function 4: Return a string like "CCoCodCode" for a given string
def string_splosion(string):
    result = ""
    for i in range(len(string) + 1):
        result += string[:i]
    return result

# Function 5: Count the number of times a substring length 2 appears in the string and also as the last 2 chars
def last2(string):
    if len(string) < 2:
        return 0
    last_2 = string[-2:]
    count = 0
    for i in range(len(string) - 2):
        if string[i:i+2] == last_2:
            count += 1
    return count

# Function 6: Return the number of 9's in the array
def array_count9(nums):
    return nums.count(9)

# Function 7: Return True if one of the first 4 elements in the array is a 9
def array_front9(nums):
    return 9 in nums[:4]

# Function 8: Return True if the sequence of numbers 1, 2, 3 appears in the array
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False

# Function 9: Return the number of positions where two strings contain the same length 2 substring
def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count