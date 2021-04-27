### Lesson 6 - scope

### global scope
x = 300
def myfunc():
    print(x)
myfunc()
print(x)

### function scope
x = 300
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)

### global keyword
x = 300
def myfunc():
    global x
    x = 200
    print(x)
myfunc()
print(x)
