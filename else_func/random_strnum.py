import random

def random_strnum(n):
    con = ''
    
    for i in range(n):
        con += str(random.randint(0,9))
    
    return con
