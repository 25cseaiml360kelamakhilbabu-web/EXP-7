# Question 5
# WAP to convert a given list of integers and a tuple of integer in a list of string using map().
words = dict(enumerate("one two three four five six seven eight nine".split()))
convert = lambda l: words.get(l, "zero")

l1 = list(eval(input("enter the number list:")))
print(list(map(convert, l1)))

l1 = tuple(eval(input("enter the no of tuple:")))
print(list(map(convert, l1)))