#import module starting.py

import starting_module

# import module starting.py and make an alias
import starting_module as first

starting_module.sayHi('OM SHREE ')
first.sayHi('OM SHREE ')

x=starting_module.player1['name']
x=first.player1['name']
print(x)

#import random
#new_rand = random.randint
#print(new_rand(5,200))


#import platform
#x= platform.system()
#print(x)

#y=dir(platform)
#print(y)


# import a part from a module and we can do that using from keyword

from starting_module import player1
print(player1['name'])