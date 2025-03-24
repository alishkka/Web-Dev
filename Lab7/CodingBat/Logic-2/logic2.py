# Function 1: Determine if it is possible to make the goal using bricks
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - 5 * min(big, goal // 5) <= small

# Function 2: Return the sum of three values, ignoring duplicates
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b
    return a + b + c

# Function 3: Return the sum of three values, stopping at 13
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

# Function 4: Return the sum of three values, treating teens as 0 (except 15 and 16)
def no_teen_sum(a, b, c):
    def fix_teen(n):
        return 0 if 13 <= n <= 19 and n not in [15, 16] else n
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# Function 5: Return the sum of three rounded values
def round_sum(a, b, c):
    def round10(num):
        return (num + 5) // 10 * 10
    return round10(a) + round10(b) + round10(c)

# Function 6: Determine if one value is close and the other is far
def close_far(a, b, c):
    close = lambda x, y: abs(x - y) <= 1
    far = lambda x, y: abs(x - y) >= 2
    return (close(a, b) and far(a, c) and far(b, c)) or (close(a, c) and far(a, b) and far(b, c))

# Function 7: Determine the number of small bars to use to meet the goal
def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)
    remainder = goal - max_big * 5
    return remainder if remainder <= small else -1