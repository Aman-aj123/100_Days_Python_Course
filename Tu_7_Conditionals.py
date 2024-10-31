#---->  Conditional operators
# >, <, >=, <=, ==, !=, 

age = int(input("Enter your age !"))
 

# --> nested statement
if(age> 18) :  
    if(age == 19) :
        print("Your age is nineteen")
    elif(age > 20 ): 
        print("Your age is greater than twenty...")
    else: 
        print("Your age is greater than 18..")
        
elif(age < 18):
    print("Your age is less than eighteen..")
        
else : 
    print("Your age isn't elegible so, you can't drive..")