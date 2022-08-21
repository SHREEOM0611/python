# class construction

class Newclass:
    def newfun(self):
        return 'PYTHON is fun!'



# object craetion
first_obj = Newclass()
print(first_obj.newfun())



# create multiple object of a class
second_obj = Newclass()
print(second_obj.newfun())
third_obj = Newclass()
print(third_obj.newfun())
fourth_obj = Newclass()



# more than one function in a class

class Domath:
    def addition(self,x,y):
        return x+y
    def multiply(self,x,y):
        return x*y
    def division(self,x,y):
        return x//y
    def difference(self,x,y):
        return x-y

first_o= Domath()

print(first_o.addition(4,2))



# constructor
# init function is called automatically every time the class is being used to create a new object.
# init function 

class NewClass:
    def __init__(self):
        print("HELLO BABY")
        self.a='VIVEKANAND'
    def hi(self):
        return "hi there!"


first=NewClass()  # print hello baby without asking for print as it is inside constructor an called while creating an object
print(first.a)
print(first.hi()) 



# methods in objects are called functions that belong to the object
# method inside class
class player:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def newHi(self):
        print("Hi, My name is " + self.name + " and age is " + str(self.age))

o1 = player('developer', 56)
o1.newHi()



# self parameter shows that the code is for any instance that created and it is not simply a local variable
# here in the example self.name means, once the object is created from the class we can access the that variable using dot notation. It is an attribute reference
# we want to access the local variable of function inside the class from our object so we used self.variable to access variable.
# self is a convention u can use anything in place of self like hey
# but try to use convention is better as it makes your code more readable to other programmers or a website




# how to delete properties

#del o1.age
#print(o1.age)


# how to delete object

#del first
#print(first.a)



# how to modify the object properties
# you can reassign the value of object property and then use it
o1.age=99
print(o1.age)