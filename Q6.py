# Question 6
# WAP to find the ratio of positive no and negative no and zero in an array of integers.
x = list(eval(input("enter the integer array")))
n = len(x)
sign = lambda y: (y > 0) - (y < 0)
sign = list(map(sign, x))
ratios = list(map(lambda k: round(sign.count(k) / n, 2), (1, -1, 0)))
print("Ratios [positive, negative, zero]:", ratios)