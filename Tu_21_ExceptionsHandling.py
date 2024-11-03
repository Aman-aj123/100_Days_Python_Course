# Exceptions handling in python




try: 
    number = int(input("Enter the number You want to generate table: "))
    for n in range(1, 11) : 
     print(f"{number} X {n} = {number * n}")
    
except Exception as e : 
    print("Some error occurs with : ", e)
    
    
    
print("Ending Here...")