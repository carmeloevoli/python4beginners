# Lesson 2 - data_types

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool

### 0: Get data type
x = 5 # case-sensitive X is not x
print(type(x))

### 1: data type is assigned (and can change) at execution time

# Text type:
x = "Hello World" # is the same as 'Hello world'

# Numeric types:
x = 20
x = 20.5
x = 1j

# assign values to multiple variables in one line:
x, y, z = "Berlin", "Paris", "Rome"
print(x)
print(y)
print(z)

# assign the same value to multiple variables in one line:
x = y = z = "Paris"
print(x)
print(y)
print(z)

# Sequence types:
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6) # x = range(2,6)
 
# Mapping types:
x = {"name" : "John", "age" : 36}

# Set types:
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})

# Boolean types:
x = True

### 2: specify the data type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)

### 3: float numbers
x = 1.10
y = 35e3
z = -12E4

print(type(x))
print(type(y))
print(type(z))

### 4: complex numbers
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

### 5: type conversion / casting
x = 1    # int
y = 2.8  # float

a = float(x)
b = int(y)

print(a,b)
print(type(a), type(b))

### 6: string<->float conversion
a = float("4.2")
b = str(2)

print(a,b)
print(type(a), type(b))
