# Question 1WAP to triple all numbers in a given list of integers, use map().   
# Answer:
Pythonx = list(eval(input("enter a list")))
def triple(x):
    return x * 3

y = list(map(triple, x))
print(y)
