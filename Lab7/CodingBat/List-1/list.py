# Function 1: Return True if 6 appears as either the first or last element in the array
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

# Function 2: Return True if the first and last elements are equal
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

# Function 3: Return an array containing the first 3 digits of pi
def make_pi():
    return [3, 1, 4]

# Function 4: Return True if two arrays have the same first or last element
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

# Function 5: Return the sum of all elements in an array of length 3
def sum3(nums):
    return sum(nums)

# Function 6: Return an array with elements rotated left
def rotate_left3(nums):
    return nums[1:] + nums[:1]

# Function 7: Return an array with elements in reverse order
def reverse3(nums):
    return nums[::-1]

# Function 8: Return an array where all elements are set to the larger of the first or last element
def max_end3(nums):
    max_val = max(nums[0], nums[-1])
    return [max_val, max_val, max_val]

# Function 9: Return the sum of the first 2 elements in the array
def sum2(nums):
    return sum(nums[:2])

# Function 10: Return a new array containing the middle elements of two arrays
def middle_way(a, b):
    return [a[1], b[1]]

# Function 11: Return a new array containing the first and last elements of the original array
def make_ends(nums):
    return [nums[0], nums[-1]]

# Function 12: Return True if the array contains a 2 or a 3
def has23(nums):
    return 2 in nums or 3 in nums