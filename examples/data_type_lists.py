# data types in Python used to store collections of data are: lists, Tuple, Set, and Dictionary
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

# make a list
thislist = ["apple", "banana", "apple", "cherry", "frog", "avercene"] # allow duplicate!
thislist = list(("apple", "banana", "apple", "cherry", "frog", "avercene"))
print(thislist)
print(len(thislist))

# access items
print(thislist[0])
print(thislist[-1])
print(thislist[0:2])
print(thislist[:4])
print(thislist[3:])

# check if item is present
print("apple" in thislist)

# change elements
thislist[1] = "monkey"
thislist[1:3] = ["blackcurrant", "watermelon"]

# insert elements
thislist.append("bob")
print(len(thislist))

thislist.insert(2, "watermelon")
print(thislist)

# remove elment
thislist.pop(1)
print(thislist)

thislist.remove("watermelon")
print(thislist)

while("watermelon" in thislist):
    thislist.remove("watermelon")
   
print(thislist)

thislist.clear()

thislist.reverse()
print(thislist)

thatlist = ["abc", 34, True, 40, "male"]
print(type(thatlist))

# loop through list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

for i, item in enumerate(thislist):
    print (i, item)
