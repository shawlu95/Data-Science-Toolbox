from functools import reduce
from itertools import accumulate

lis = [1, 2, 3, 4]

# no need to convert to list, as required by map and filter
product = reduce(lambda x, y: x * y, lis)
print(product)

# use accumulate to get all intermediate steps
accum = list(accumulate(lis, lambda a, b: a * b))
print(accum)

# using reduce to compute maximum element from list
print ("The maximum element of t[he list is : ",end="")
print (reduce(lambda a, b : a if a > b else b, lis))

