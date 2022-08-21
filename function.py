# a func is a group of code or a group of statement which only run when we call it and perform a specific task. We can pass data or parameters in func and break the program in smaller junks.
# it can return data as final result

def helo_function():
    print(" hello from function")
    return 0

#print(helo_function())
#helo_function()
# 0 is also printed as we print(0) is the meaning of print(hello_function()) after the print inside the function completed

name=input("what is your name? ")
#pass arguement into a function
def hello_function(abc ="HELLO"):
    print("HELLO "+ abc)
    

hello_function(name)
hello_function("BABY")
hello_function()


# you can pass anything as an arguement string, tuplr, list etc.
# passing list as an arguement
fruits=["mango",'apple',"guava","papaya"]
def food(fru):
    for x in fru:
        print(fru)
        print(x)
        print(x[1])
    return "NARCOS"

food(fruits)
print(food(fruits))


a=10
def hell(a):
    return a*10
print(hell(a))

# it can return no. of things
def add(a, b):
    return a+5, b+5
result = add(3, 2)
print(result)

a=20
b=30
c=5


# giving the indication so that the other programmer will use which data type it can give. you can ignore it it doesn't matter. this process is called type hinter
def findMax(a:int,b:int,c:int):
    if (a>=b and a>=c):
        return a
    if (b>=a and b>=c):
        return b
    if (c>=b and c>=a):
        return c

print(findMax(a,b,c))
    