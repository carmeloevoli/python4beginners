# Lesson 1 - operators

# variable assignment
a, b = 10, 5
a, b = b, a
c = a + b

print(c)

# arithmetic operators:
# Addition: +
# Subtraction: -
# Multiplication: *
# Division: /
# Modulus: %
# Exponentiation: **
# Floor division: //

x = 18
x = x - 2
x -= 2

x = x ** 3 # better using numpy
x **= 3

print(x)

# comparison operators:
# Equal: ==
# Not equal: !=
# Greater than: >
# Less than: <
# Greater than or equal to: >=
# Less than or equal to: <=

# logical operators:
# and
# or
# not

x = 5
print(x > 3 and x < 10)
print(3 < x < 10)

# identiy operators:
# is
# is not

a = 'Freghete'
b = 'Ofreghete'
c = 'Freghete'

print(a is c)
print(a is b)
print(a is not b)

# membership operators:
# in
# not in
a = 'Hello world'
b = 'Hello'

print(b in a)

Europe = ['Italy', 'France', 'Germany', 'Portugal', 'Spain', 'Belgium', 'Slovenia'] # list

print ('Britain' in Europe)
