# Question 2WAP to add three given list using python map and lambda.
# Answer:
Pythonx = list(eval(input("enter the 1st list")))
y = list(eval(input("enter the 2nd list")))
z = list(eval(input("enter the 3rd list")))
print("original list")
print(x)
print(y)
print(z)

l1 = list(map(lambda x, y, z: x + y + z, x, y, z))
print("The resultant list is:", l1)
