# parse, read, write json. Json stands for JavaScript object notation.
# Json, is a syntax for storing and exchanging data also.


#converting JSON to PYTHON
#import json5
# adding some json
#player1= {"name":"Dhoni", "age":35, "city":"ranchi"}
#parse
#x = json5.loads(player1)

# display the output
#print(x["name"])



# converting json from python
#import json5
# create python dictionary
#player1= {"name":"Dhoni", "age":35,"city":"ranchi"}
# converting into json
#y= json5.dumps(player1)
 
 # output
#print(y)


#You can convert Python object type into json string type.
# you can call the python object types like dictionaries, lists, tuples, strings, integers, float, and none, too, just on the strings formula.

# python object to json string
#import json5
#print(json5.dumps({"name":"Dhoni", "age":35,"city":"ranchi"}))
#print(json5.dumps(["orange", "lemon"]))
#print(json5.dumps(("orange", "lemon")))
#print(json5.dumps("hi there"))
#print(json5.dumps(55))



#@ parse from file
#import json5

#with open ('player.json') as f:
#    data = json5.load(f)

# output
#print(data)

# json.dump

import json5

player1= {"name":"Dhoni", "age":35,"city":"ranchi"}

# open file in write mode
with open("player1.txt","w") as json_file:
    json5.dump(player1, json_file)

# enhance json indent, sort_key
player_dict=json5.loads(player1)

# displayng output
print(json5.dumps(player_dict, indent=4, sort_keys=True))