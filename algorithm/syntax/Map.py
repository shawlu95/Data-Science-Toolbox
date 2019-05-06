def calculateSquare(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


numbers = (1, 2, 3, 4)
result = map(lambda x: x * x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))


# iterate over multiple function (stupid)
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)