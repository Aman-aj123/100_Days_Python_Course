# Math case in python

number = int(input('Enter your number !'))

match number: 
     case 0 : 
         print("You number is zero !")
     case 1 :
         print("Your number is one") 
     case 10 :
         print("Your number is ten !")

# They'll run in defualt
     case _ if number!=20 : 
        print(number, "is not twenty")
     case _ if number!=50 :
        print(number, "is not fifty")
        
     case _: 
         print("Your number is nice")
        