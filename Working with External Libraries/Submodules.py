import numpy

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

print(type(rolls))

print(dir(rolls))

# If I want the average roll, the "mean" method looks promising...

print(rolls.mean())

# Or maybe I just want to turn the array into a list, in which case I can use "tolist"

rolls.tolist()

print(rolls)


print(rolls + 10)