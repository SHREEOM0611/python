# 'try' lets you test the block for error
# 'except' block lets you handle the error
# an excpetion is an event that occurs during the execution of program that disrupts the normal flow of program's instructions

#An exception is a python object that represents an error when a Python script raises an exception, it
#must either handle the exception immediately or otherwise it terminates.
c=2
a=1
try:
    print(a)
except:
    print("This is an exception!!")


# we can use no. of exception as many as we want
try:
    print(c)
except NameError :
    print("Variable c is not defined")
except:
    print("This is an exception!!")



# how to use else keyword if no errors were raised
# if there is an error in try then you can't see the else part
try:
    print("Python is fun1")
except:
    print("AN error")
else:
    print("Everything is good and nothing went wrong")


# Finally block . this block will be executed regardless of the try is executed , error is found or not
try:
    print(c)
except NameError :
    print("Variable c is not defined")
except:
    print("This is an exception!!")

finally:
    print('Exception handling is completed')
    print('hello')



# raise keyword
d=3
if d<0:
    raise Exception("Soory, no numbers below zero hero! ")



# raise type error

e="this language is fun!"
#e=10

if not type(e) is int:
    raise TypeError("only integers are allowed here!!")





# always remember that the python copiker will show the 1st error 1st. doesnt tell the error in each line so be careful and remember that