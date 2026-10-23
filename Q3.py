# Question 3
# WAP to create a list containing the power of said numbers in leases raised to the corresponding
#  numbers in index using power from math import ...
from math import pow
x = list(eval(input("enter the powers")))
y = list(eval(input("enter the number list")))

def power(n, y):
    l = int(pow(y, n))
    return l

l = list(map(power, x, y))
print("Result =", l)