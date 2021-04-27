# Lesson 3 - containers

# data types in Python used to store collections of data are:
# lists, Tuple, Set, and Dictionary

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

### make a list
thislist = ["quark", "lepton", "meson", "quark", "photon", "neutrino"] # allow duplicate!
thislist = list(("quark", "lepton", "meson", "quark", "photon", "neutrino"))
print(thislist)
print(len(thislist))

### access items
print(thislist[0])
print(thislist[-1])
print(thislist[0:2])
print(thislist[:4])
print(thislist[3:])

### check if item is present
print("lepton" in thislist)
print("wimp" in thislist)

### change elements
thislist[1] = "higgs"
thislist[1:3] = ["higgs", "muon"]
print(thislist)

### insert elements
thislist.append("tau")
print(len(thislist))

thislist.insert(2, "higgs")
print(thislist)

### remove elements
thislist.pop(1)
print(thislist)

thislist.remove("tau")
print(thislist)

while("quark" in thislist):
    thislist.remove("quark")
print(thislist)

thislist.clear()
print(thislist)

### reverse elements
thislist = ["quark", "lepton", "meson", "photon"]
thislist.reverse()
print(thislist)

### mixed types list
thatlist = ["quark", 1492, True, 0.938, "Heisenberg"]
print(type(thatlist))

### loop through list

for i in range(len(thislist)):
    print(thislist[i])

for x in thislist:
    print(x)
    
for i, item in enumerate(thislist):
    print (i, item)

[print(x) for x in thislist]

### list comprehension
### syntax: newlist = [expression for item in iterable if condition == True]

particles = ["quark", "lepton", "meson", "photon", "wimp"]
existingparticles = []

# long method:
for x in particles:
    if not "w" in x:
        existingparticles.append(x.upper())
print(existingparticles)

# compact method:
existingparticles = [x.upper() for x in particles if not "w" in x]
print(existingparticles)

### tuples
particles = ("quark", "lepton", "meson", "photon", "wimp")
print (type(particles))

### tuples cannot be changed
#particles[1] = "pippo" ! not allowed

### tuples unpacking
(h, l, *m) = particles
print(h)
print(l)
print(*m)

### dictionary
electron = {
    "elementary": True,
    "mass": 0.51099895000e6,
    "spin": 1/2,
    "discovered_by" : "Zichichi",
    "interactions" : ('gravity', 'electromagnetic', 'weak')
}

print(electron)
print(electron["mass"])

### change element dictionary
electron["discovered_by"] = 'Rutherford'
electron.update({"interactions": ('gravity', 'electromagnetic', 'weak', 'supersymmetry')})

print(electron)

### loop dictionary
for x in electron: # keys
    print(x)

for x in electron: # values
    print(electron[x])

for x in electron.values():
    print(x)
    
for x in electron.keys():
    print(x)

for x, y in electron.items():
    print(x, y)
