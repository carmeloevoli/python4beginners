### Lesson 8 - file handling

def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

modulus, a, c = pow(2, 32), int(1664525), int(1013904223)
seed = int(123456789)
rand = lcg(modulus, a, c, seed)

### write a file
f = open("demofile.txt", "w")
for i in range(10):
    value = next(rand)
    f.write(str(i) + " " + str(value) + "\n")
f.close()

### reading a file
f = open("demofile.txt", "rt") # (r)eading a (t)ext file
print(f.read())
print(f.readline())
for x in f:
    print(x)
f.close()
