# Function 1: Determine if the squirrel party is successful
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (is_weekend or cigars <= 60)

# Function 2: Determine the result of getting a table at a restaurant
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

# Function 3: Determine if squirrels play based on temperature and season
def squirrel_play(temp, is_summer):
    upper_limit = 100 if is_summer else 90
    return 60 <= temp <= upper_limit

# Function 4: Determine the result of being stopped by a police officer
def caught_speeding(speed, is_birthday):
    speed_limit = 5 if is_birthday else 0
    if speed <= 60 + speed_limit:
        return 0
    elif speed <= 80 + speed_limit:
        return 1
    else:
        return 2

# Function 5: Return the sum of two numbers, with forbidden range handling
def sorta_sum(a, b):
    total = a + b
    return 20 if 10 <= total <= 19 else total

# Function 6: Determine the alarm clock time based on the day and vacation status
def alarm_clock(day, vacation):
    if vacation:
        return "off" if day in [0, 6] else "10:00"
    else:
        return "10:00" if day in [0, 6] else "7:00"

# Function 7: Determine if the number 6 is "great" based on given conditions
def love6(a, b):
    return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6

# Function 8: Determine if a number is in the range 1..10 based on mode
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

# Function 9: Determine if a number is within 2 of a multiple of 10
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8