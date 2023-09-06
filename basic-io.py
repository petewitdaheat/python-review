# the print function prints its parameter to standard out
#and appends a line separator string to the end
print("Hello World")

# the print method may print its parameterwithout appending
# a line separator string to the end using the end parameter
print("Hello World", end=" ")
print("Hello World")


# the print function may be given strings as well as any of the primitive and object types
print(100)
print(True)
print(100.75)

# we can pass one or more parameters when using the print function
# by default, they will be separated by a space
print(100, True, 100.75)

# the default space can be modified and can be made to change to 
# any characters, integer, or string using the sep parameter.
print(100, True, 100.75, sep="-")

# The sep and the end parameters may be used together in one print statement.
print(100, True, 100.75, sep="-", end="!")

# The string % modulo operator can be used with the print function
# for formatting
print("\nHello %s %s. You are %d years old." % ("Peter", "Calandra", 21))
print("Hello %s %s. You are %.2f years old." % ("Peter", "Calandra", 21.5))

# the input function can be used to get data from the standard in.
# the returned object will always be a string.
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
print(first, last)

age = input("Please enter your age: ")
print("Hello %s %s. You are %s years old." % (first, last, age))
# This line of code will generate a TypeError because age is a string
#print("Hello %s %s. You are %.2f years old." % (first, last, age))
print(type(first), type(last), type(age))

# we must type cast the returned object if we want to woek with
# it in a form other than string
intage = int(input("Please enter your age: "))
print("Hello %s %s. You are %d years old." % (first, last, intage))
floatage = float(input("Please enter your age: "))
print("Hello %s %s. You are %.2f years old." % (first, last, floatage))

# The split function can be used to get multiple values from standard in. 
# If a separator isn't given to the function, then a white space is used.
fname, lname = input("Enter your first and last names separated by a space: ").split()
print(fname, lname)

# a separator, like a comma, may be provided.
fname, lname, tn = input("Enter your first and last name and telephone number separated by a space: ").split(",")
print("Hello %s %s. Your phone number is %s." %(fname, lname, tn))

# We can take in a variable number of inputs at a time.
x = [int(x) for x in input("Enter multiple numbers separated by a space: ").split()]
print("Numbers are: ", x)