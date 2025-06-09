# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
# tuple is immutable means can't be changed
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])

# use slices to get parts of a sequence
print(mylist[1:3])
print(mylist[1:5:2])

# you can use slices to reverse a sequence
print(mylist[::-1])
# default start and end with -1 for reverse

# dictionaries are accessed via keys
print(mydict["one"])
print(mydict["two"])

# ERROR: variables of different types cannot be combined
print("my string" + str(12))

# Global vs. local variables in functions
def main():
    mystr = "test local"
    print(mystr)

main()
print(mystr)
