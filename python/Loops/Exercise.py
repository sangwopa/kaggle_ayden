def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return bool(sum([num % 7 == 0 for num in nums]))

nums = []

print(has_lucky_number(nums))

def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    con = []
    return([con > thresh for con in L])

print(elementwise_greater_than([1, 2, 3, 4], 2))

def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

#And here's the list comprehension version:

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    i = 0
    while i < len(meals) - 1:
        if meals[i] == meals[i + 1]:
            return True
        i += 1
    return False

meals = [1,1,2,3,4,5,6]

print(menu_is_boring(meals))

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    sum = 0
    for i in range(n_runs):
        sum += play_slot_machine()
    return (sum - n_runs)/n_runs