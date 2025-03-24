# Function 1: Return a string where every char is doubled
def double_char(s):
    return ''.join([c * 2 for c in s])

# Function 2: Return the number of times "hi" appears in the string
def count_hi(s):
    return s.count("hi")

# Function 3: Return True if "cat" and "dog" appear the same number of times
def cat_dog(s):
    return s.count("cat") == s.count("dog")

# Function 4: Return the number of times "code" appears with any letter for 'd'
def count_code(s):
    return sum(1 for i in range(len(s) - 3) if s[i:i+2] == "co" and s[i+3] == "e")

# Function 5: Return True if either string appears at the end of the other (case insensitive)
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)

# Function 6: Return True if "xyz" appears without being preceded by a period
def xyz_there(s):
    return "xyz" in s.replace(".xyz", "")