# Are values being rounded on assignment and during calculations?
a = 1/10
print("%.64f"%a)

# decimals are rounded off!
b = 1.2 ** 308
print("%i"%b)

# round off, when add 1 to a very small number
c = 0.5 ** 100
print("%.128f"%c)
print("%.128f"%(c + 1))

# this is close to double ~9 x10^-307 to ~2 x10^308
# unsigned
import sys
print("%i"%sys.float_info.max)
print("%i"%(sys.float_info.max - 1))

# can get very close to zero
print(sys.float_info.min)
print("%.500f"%0)

# exceptional value: infinity
print(sys.float_info.max * 2)
print(sys.float_info.max * 1.1)
print(sys.float_info.max * 2 - sys.float_info.max - sys.float_info.max)

print(sys.float_info.max + sys.float_info.min)
print(sys.float_info.max - 1)

print(type(c))

crazy = 10**9999
print(c)
# print(1.9**310 + 666**666)
print(1.7976931348623157e+308 + 1.7976931348623157e+308)
# error: division by zero
# print("%f"%(1/0))