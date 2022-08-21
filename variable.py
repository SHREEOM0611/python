# variable declaration and assignment
name ="Ronaldo"
num = 7
age = 34

# multi-assignment within a single statement
name1, num1, age1 = "Messi", 8, 36

# get the output

print(name1)
print(num1)
print(age1)
print(name, num, age)

print(" The player name is",name,", his age is ", age," and his jersey number is",num)

# error in below line
#  print("The player name is "+name + "and his age is" +age)
# cannot concatenate the string and integer file
# we can convert the integer into string and then concatenate
print("The player name is "+name + " and his age is " +str(age))


x=7
y=4.5
z=x+y
print(type(z))