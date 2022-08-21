# create dictionaries

no_fruits = {"banana" : 12, "apple" : 20, "mango" : 10}
print(no_fruits)
print(type(no_fruits))

# another way to create dictionaries
no_fruits = dict({"banana" : 12, "apple" : 20, "mango" : 10})
print(no_fruits)
print(type(no_fruits))

print(no_fruits["apple"])
print(no_fruits.get("banana"))

no_fruits = dict({"banana" : [12,10,8], "apple" : 20, "mango" : 10})
print(no_fruits["banana"][1])
print(no_fruits.get("banana")[1])


#updating dictionary
no_fruits["banana"]=15
print(no_fruits)

# add item
no_fruits["peach"]= 15
print(no_fruits)

# deleting an element in dictionary
del no_fruits["apple"]
print(no_fruits)

#deleting the whole dictionary
del no_fruits
print(no_fruits)