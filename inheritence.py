# inheritence defines a class that inherits all the methods and properties from another class
# child class vs parent class . child class inherits the properties and functions from the parent class







# parent class
class anyone:
    def __init__(self,first_name,last_name):
        self.f_name = first_name
        self.l_name = last_name

    def display(self):
        print("Hi, My name is " + self.f_name + self.l_name)
# object
bro = anyone("parth"," jha")
bro.display()

# child class
class player(anyone):
    pass

o1= player("raju"," shrivastav")
o1.display()


