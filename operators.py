#operators are used to calculate variables,compare values, join strings together, assign values to variable,



# ARITHMETIC OPERATORS
# calculate the equation arithmetically and give us appropriate answer
#print(100 + 70)  #addition
#print(100 - 70)  # substraction
#print(100 * 70)  # multuiplication
#print(100 / 50)  # final result is of float datatype
#print(100 // 50) # as the final answer in division was coming float so, this is used for integer answer. It only gives integer value of the respective answer.
#print(100 % 70)  # modulo
#print(10 ** 3)   # power print 10^3


# COMPARISON OPERATORS
# will give the output as true or false after comparing
#print(3==3)  # is equal to
#print(2==3)  # is equal to
#print(2!=3)  # is not equal to
#print(2<3)   # is smaller than
#print(20>=10) # is greater than or equal to
#print(30<=20) # is smaller than or equal to


# LOGICAL OPERATORS
# it perform the task logically.  AND, OR, NOT
#print(5==5 and 10==10)
#print(5==5 and 10==20)
#print(5==5 or 10==10)
#print(5==5 or 10==20)
#print(5==10 or 10==20)
#print(not True)
#print(not (5==10 or 10==20))


# ASSIGNMENT OPERATORS

x=5+10
#print(x)

y=10
y+=5
#print(y)

z=5
z/=2
#print(z)



# CONDITIONAL OPERATORS
name="Python"
#print("False!" if name != "Python" else "True")
#print("True!" if name != "Python" else "False")
#print("XYZ!" if name != "Python" else "ABC")

# TERNARY OPERATORS
a=10
print("Smaller than 10" if a<10 else"Anything else")
b= 24 if a>5 else 20
print(b)
