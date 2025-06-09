#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def hello():
    print("this is a function")

# TODO: function that takes arguments
def func1(a, b):
    print(a, b)

# TODO: function that returns a value
def cube(x):
    return x * x * x 

# TODO: function with default value for an argument
def power(num, x=1):
    res = 1
    for i in range(x):
        res = res * num
    return res

# TODO: function with variable number of arguments
def multi(*args):
    res = 0
    for x in args:
        res = res + x
    return res



hello()
print(hello())
# no return value so none

func1(3, 5)
print(cube(3))

print(power(2))
print(power(2, 3))

print(multi(3,4,6,2,2))
print(multi(3,4,6,2,2,10))