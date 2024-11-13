import random


ask = input("What do you want 'Code' or 'deCode' ? ")
name = input("Enter the name !")


  
def Code(name) :
  if (len(name) > 3 ) : 
      slicedName = name[1:] + name[0]
      randomWords = "AbCdEeFfGgHhIiJjKkLlMnOoPpQqRrSsTtUuVvWwXxYyZz"
     
     
      for i in range(1, 4) : 
            random_int = randomWords[random.randint(0, len(randomWords))]
            slicedName = random_int + slicedName + random_int
    
    
      return slicedName

  else  :
        name = name[::-1]
        return name



def deCode(name) : 
         name =   name[3: len(name) - 3]  
         name = name[len(name)-1] + name
         name = name[:-1]
         return name
    

    

if (ask == "Code") : 
    a = Code(name)
    print(a)
else : 
   b = deCode(name)
   print(b)