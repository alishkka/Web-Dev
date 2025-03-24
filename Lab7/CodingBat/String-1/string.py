# Function 1: Return a greeting of the form "Hello name!"
def hello_name(name):
    return f"Hello {name}!"

# Function 2: Return the result of putting two strings together in the order abba
def make_abba(a, b):
    return a + b + b + a

# Function 3: Create an HTML string with tags around the word
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

# Function 4: Return a new string where the word is in the middle of the out string
def make_out_word(out, word):
    return out[:2] + word + out[2:]

# Function 5: Return a new string made of 3 copies of the last 2 chars of the original string
def extra_end(string):
    return string[-2:] * 3

# Function 6: Return the string made of its first two chars
def first_two(string):
    return string[:2]

# Function 7: Return the first half of a string of even length
def first_half(string):
    return string[:len(string)//2]

# Function 8: Return a version without the first and last char
def without_end(string):
    return string[1:-1]

# Function 9: Return a string of the form short+long+short
def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

# Function 10: Return the concatenation of two strings, omitting the first char of each
def non_start(a, b):
    return a[1:] + b[1:]

# Function 11: Return a "rotated left 2" version of the string
def left2(string):
    return string[2:] + string[:2]