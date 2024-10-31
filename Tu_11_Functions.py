# Functions in python
def greet() : 
    print("Hellow, I'm a function")

greet() # we're calling this function


#---------> Functions with arguments
def operation(a, b, operation) :
    if(operation == "+") :
        print(a+b)
    elif(operation == "-"):
        print(a-b)
    elif(operation == "*"):
        print(a*b)
    elif(operation == "/") : 
        print(a/b)
    else : 
        print("Plz enter a operation")
    

# we can perform all the tasks now with only calling the function with 'arguments'
operation(5, 27, "-")
operation(10, 3, "+")
operation(53, 25, "*")
operation(89, 26, "/")


#------> default arguments
def printNum(num1=10, num2=20):
    print(num1 + num2)


printNum() # It'll print the default values of the numbers
printNum(5, 2)  





def executeAfter() :
    pass # Ish ko mai baad me likhunga
    
    



def nice(*numbers) :
    num = 0
    for b in numbers :
        num += b

    print("Average is ", num/len(numbers))

nice(2, 3, 5)