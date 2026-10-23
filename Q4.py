# Question 4
# WAP to convert all the characters into uppercase and lowercase and duplicate letters from a given sequence.
def swap(y):
    if y.isupper():
        return str(y).lower()
    else:
        return str(y).upper()

y = list(eval(input("enter characters list:")))
s = map(swap, y)
print(set(s))