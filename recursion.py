# python supports recursion that a function can call itself . Be more careful 

def new_recursion(n):
    if(n>0):
        result= n + new_recursion(n-1)
        print(result)
    else:
        result=0
    return result

new_recursion(10)