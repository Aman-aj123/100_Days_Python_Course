# Finally keyword in python  ---> It alwlays executed

# try : 
#     num = input("Enter the number")
#     print(int(num) * 5)

# except : 
#      print("Some error occurs while multiplication...")
#      msg = "Sucess"
 
# finally : 
#     print("I run finally")



def Multiply() : 
    try : 
        num = input("Enter the number")
        print(int(num) * 5)
        return "Sucess"

    except : 
        print("Some error occurs while multiplication...")
        return "Failed.."
    
    finally : 
        print("I run finally")



a = Multiply()
print(a)