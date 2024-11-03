# Recursion in python

def factorise(n) : 
    if(n==0 or n==1 ) : 
        return n
    else : 
        return  n * factorise(n - 1) # we're calling the same function in the particular function
    



factorise1 = factorise(5)
print(factorise(5))  