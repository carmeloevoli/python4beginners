# This is a comment <-

"""
This is a comment 
written in more 
than just one line
"""

# 0: Simple printing
print("This is Python!")

a = 4
print(a)

# 1: Simple printing of a variable and formatting
x = 31.3280583343232523523
print(x)
print("x = {}".format(x))
print("x = {:5.2f}".format(x))
print("x = {:5.2e}".format(x))
print("a = {} and x = {}".format(a,x))
print("a = {} and x = {:5.2f}".format(a,x))

# 2: Printing more variables
name = 'Sun'
age = 4.603e9 # yr
distance = 149.42e11 # cm
mass = 1.989e33 # gr

print("my name is {} and I'm {} years old".format(name, age))
print("my name is {:s} and I'm {:5.2e} years old".format(name, age))
print("At a distance of {1:} cm I attract you having a mass of {0:}".format(mass, distance))
print("At a distance of {1:5.2e} cm I attract you having a mass of {0:5.2e}".format(mass, distance))

# 3: String concatenation
name = 'Sun'
age = 4.6 # Gyr

print('Hey my name is ' + name + ' and I am ' + str(age) + ' billions of years')

output = f'Hey my name is {name} and I am {age} billions of years'
print(output)
