
#
def player(a,b,c):
    print("The player name is " + a)
    print("The player name is " + b)
    print("The player name is " + c)


player(a="dhoni",b="sachin",c="virat")


# arbitary arguement
def new_a(*player):
     print("The player is " + player[2])


new_a("dhoni","sachin","virat")


