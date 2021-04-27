### Lesson 4 - codeblocks

### if - else block
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

### if - single line
if a > b: print("a is greater than b")

### if - else single line
print("A") if a > b else print("B")

### and or
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

### while block
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# also break and continue but very bad programming style!

### for block
for x in range(0, 10, 2):
    print(x * x)
else:
    print("Finally finished!")
