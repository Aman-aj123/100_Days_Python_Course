timeStr = int(input("Enter your time! "))


if(timeStr>0 and timeStr<12) : 
    print("Good morning sir !")

elif(timeStr >= 12  and timeStr < 17) : 
    print("Good Afternoon sir !")
    
elif( timeStr>17 and timeStr < 20) : 
    print("Good evening sir !")
    
elif(timeStr>20 and timeStr < 24) :
    print("Good night sir !")