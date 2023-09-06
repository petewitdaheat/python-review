# expressions in python evaluate to true or false
#expressions use the comparison operators: <,
# >, <=, >=, ==, !=

x = 4
print(x < 5)
print(x > 5)
print(x == 5)
print(x != 5)

# python supports the if, if-else, if-elif-else, and 
#nested if decisions

# The if decision structure tests its condition
# and if the condition is true, it executes the code.
# block its given
if (x < 5):
    print("x is less than 5 is true")
# here is the shortand version
# shorthand version may be used when there is only one 
# statement to be executed.
if (x < 5): print("x is less than 5 is true")

# the if-else decision structure tests its condition
# and if the condition is true, it executes the code block
# it's given. if the condition is false, the code block
# given to the else is executed.
if (x == 5):
    print("x is equal to 5 is true.")
else:
    print("x is equal to 5 is false.")

# here is the shorthand version of the if-else decision.
print("x is equal to 5 is true.") if (x == 5) else print("x is equal to 5 is false.")

# the if-elif-else decision structure tests multiple
# conditions. the code block given to the conditions that's true is executed
#If none of the conditions are true, the code block given to the else is executed.
if (x > 5):
    print("x is greater than 5 is true.")
elif(x == 5):
    print("x is equal to 5 is true.")
else:
    print("None of the conditions are true.")


if (x > 5):
    print("x is greater than 5 is true.")
elif(x == 5):
    print("x is equal to 5 is true.")
elif(x < 5):
    print("x is less than 5 is true.")
else:
    print("None of the conditions are true.")


if (x > 5):
    print("x is greater than 5 is true.")
elif(x == 5):
    print("x is equal to 5 is true.")
elif(x < 5):
    print("x is less than 5 is true.")
elif (x != 5):
    # this code block won't be executed even
    #though its condition is true because only 
    # the first true code block will be executed.
    print("x is not equal to 5 is true.")
else:
    print("None of the conditions are true.")


# a nested if decision is an if statement that is the target
# of another if statement
if (x < 5):
    print("x is less than 5 is true.")
    if(x != 5):
        print("x is equal to 5 is true.")


# Comparison operators may be chained together.
a = 5
b = 10
c = 15

if a < b < c:
    print("B is bigger than a and less than c.")


# python supports the match-case decision structure.
# this decision structure is useful when many conditions need to be tested.
# it requires python 3.10 or newer.
grade = "A"

match grade:
    case "A":
        print("Super work!")
    case "B":
        print("Good Job!")
    case "C":
        print("You made it.")
    case "D", "F":
        print("Oh dear...")
    case _:
        # the underscore character is used to catch
        # any cases that are not equivalent to the match
        print("Invalid grade.")


# python supports the ternary operator.
result = "x is equal to 5 is true." if (x == 5) else "x is equal to 5 is false"
print(result)
print(("x is equal to 5 is true." if (x == 5) else "x is equal to 5 is false"))

# the ternary operator may be written using tuples.
# (false value, true value) [expression to test]
result = ("x is equal to 4 is false", "x is equal to 4 is true.") [x == 4]
print(result)

# The ternary operator may be written using dictionaries.
result = {True: "x is equal to 5 is true.", False: "x is equal to 5 is false"} [x == 5]
print(result)


# expressions in pyhton may also use the logical operators:
# and, or, and not.
num = 150

# this if-else decision structure tests if num is between 1 and 100.
if (num >= 1 and num <= 100):
    print(" num is between 1 and 100.")
else:
    print("num is not between 1 and 100.")

# this if-else decision structure tests if num is not between 1 and 100.
if (num < 1 or num > 100):
    print("num is not between 1 and 100.")
else:
    print("num is between 1 and 100.")

foundIt = False

# This if-else decision structure tests if foundIt is False
if (not foundIt):
    print("foundIt is false.")
else:
    print("foundIt is true.")