### Lesson 5 - functions

### a simple function
def my_function():
    print("Ciao! I'm your function")

my_function()

### argument
def print_square(value):
    print(value * value)

print_square(2)
print_square(3.14)
print_square(2 + 4j)

def compute_square(value):
    s = value * value
    return s

x = compute_square(2)
print(x)

x = compute_square(3.14)
print(x)

x = compute_square(2 + 4j)
print(x)

def full_name(name, surname):
    print(name + " " + surname)

full_name("Marie", "Curie")
full_name(surname="Dawkins", name="Richard")

### arbitrary arguments
def scientists(*names):
    print("My fav scientist is " + names[2])

scientists("Galileo", "Born", "Einstein", "Zichichi")

### default parameter value
def my_country(name, country = "Italy"):
    print("I am " + name + " from " + country)

my_country("Chandrasekhar", "India")
my_country("Carmelo")

### specifyng types
def great_scientist(name: str, born: int, died: int) -> list:
    print('age = ', died - born)
    return [name, born, died]
    
scientist = great_scientist("Galileo", 1564, 1642)
print(scientist)

#scientist = great_scientist(1564, 1642, "Galileo") ! wrong
