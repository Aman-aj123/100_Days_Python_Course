# Tuples cannot be changed

nice = (1, 2, 3, 4, 5, 6)
# nice[0]  = "Aman" ----> We can't do like this !

sliceTuple = nice[0: 3]
print(sliceTuple)
print(nice.count(1))
 

# if 6 in nice :
#     print("6 is available...")

# else : 
    # print("6 isn't available...")