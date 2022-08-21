# creating a list

player = ["DHONI","SACHIN","VIRAT","JADEJA" ]
print(player)

mixed = ["DHONI",[3,7,11], 28, True]
print(mixed)

print(len(player))
print(player[0])
print(player[1])
print(player[2])
print(player[3])

print(player[0:-2])
print(player[0:2])
print(player[0:4])
# print(player[-1:3]) not working why? logical error ig!
print(player[-1])

# using random function in list
import random
print(random.sample(player,3))
print(random.choice(player))

player[2]="BRIAN"   # changes the 3rd index which index no. 2
print(player)
player.append("Another Player")
print(player)

player.insert(3,"brian")
print(player)


