import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)

print(rolls)

print(rolls + 10)

print(rolls <= 3)

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)

print("xlist = {}\nx =\n{}".format(xlist, x))

print(x[1,-1])

print(xlist[1,-1])