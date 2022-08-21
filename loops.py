# while loop

num = 1 
while (num<8):
    #print(num)
    #print(num-1)
    num +=1

# break statement berak the previous while loop
num = 1 
while (num<8):
   # print(num)
    #print(num-1)
    num +=1
    if num==4:
        break


# while else
num = 1 
while (num<8):
    #print(num)
    #print(num-1)
    num +=1
else:
    print("Loop is completed")

# if you break the loop using break statement then the else part will not be executed even if it should be
num1 = 1
while (num1<8) :
    #print(num1)
    num1 = num1 + 1
    if num1== 4:
        break
       
#else:
  # print("Loop is over")

# positioning increment or decrement 
num = 1 
while (num<8):
    num +=1
    #print(num)
    #print(num-1)


 # for loop iterate over a sequence of variables such as integers, tuple, list etc

player = ["DHONI","SACHIN","VIRAT","JADEJA" ]
for X in player:
   # print(X)
    if X=="VIRAT":
     break


#for i in range(10):
  # print(i)

#for i in range(5,10):
 #   print(i)

#for i in range(3,10,2):
   # print(i)

   