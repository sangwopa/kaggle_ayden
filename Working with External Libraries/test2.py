a = ['J', 'A', 'A', '2']

len1 = len(a) - 1

while len1 >= 0:
    if a[len1] == 'A':
        a.pop(len1)
        a.append('A')
    len1 -= 1

print(a)
