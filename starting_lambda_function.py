
#  small anonymous function means function is without a name. It can take multiple arguements but can only have one expression means one line of code and then return
a= lambda x: x+20
a=lambda x: x+20
print(a(10))

# lambda arguements
p=22
q=30
store_lambda = lambda x, y: x*y
print(store_lambda(10,20))
print(store_lambda(p,q))

store_args= lambda x,y,z: x+y+z
print(store_args(10,20,12))



# how to use lambda function inside any other user function

def new_add(k):
    return lambda x: x+k


add1= new_add(1)
add2=new_add(2)
print(add1(12))
print(add1(20))



def add(a, b):
    return a+5, b+5
result = add(3, 2)
print(result)