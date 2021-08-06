def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

# if total_candies == 1:
#     print("Splitting 1 candy")
# else:
#     print("Splitting", total_candies, "candies")
# Here's a slightly more succinct solution using a conditional expression:

# print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or ((rain_level < 5) and have_hood) or not ((rain_level > 0) and is_workday)

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

def concise_is_negative(number):
    return (True if number < 0 else False)

def con_is_neg(num):
    return num < 0

print(concise_is_negative(0))
print(con_is_neg(-4))
