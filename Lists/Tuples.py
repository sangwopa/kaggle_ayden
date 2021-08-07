t = (1, 2, 3)

print(t)

print(type(t))

#They cannot be modified (they are immutable).

x = 0.125

print(x.as_integer_ratio()) #returns a numerator and a denominator

numerator, denominator = x.as_integer_ratio()

print(numerator)
print(denominator)
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)