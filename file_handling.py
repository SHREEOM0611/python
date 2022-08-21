# create text file
# open("fil  e name","mode")
# write()
# close()

# using write mode
f = open('hi.txt','w')

# write to hi.txt
f.write('HELLO FROM THE HI.TXT FILE !!!! ')

# close hi.txt
f.close()

# read a file using read function
f = open('hi.txt','r')
x=f.read()
print(x)
f.close()


# how to write a new text in existing file. how to write new text inside another text
f= open('hi.txt','a')
f.write(input(' \n Add the text '))
f.close()
f= open('hi.txt','r')
y=f.read()
print(y)
f.close()

