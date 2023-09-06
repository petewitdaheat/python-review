# Python supports the for and while loops.
# Loops are used to repeat a block of code.

# The for loop is used for iterating through Strings, Tuples,
# Lists, or Dictionaries.

# String
iterable = "987654321"
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# Tuple
iterable = (9,8,7,6,5,4,3,2,1)
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# List
iterable = [9,8,7,6,5,4,3,2,1]
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# Dictionaries
iterable = dict({'nine': 9,
                 'eight': 8,
                 'seven': 7,
                 'six': 6,
                 'five': 5,
                 'four': 4,
                 'three': 3,
                 'two': 2,
                 'one': 1,})
for i in iterable:
    print("%d" % (iterable[i], end=" "))
print("blastoff!")