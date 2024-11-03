# Sets in python

names = {"Aman", "Mohit", "Rohit", "Shubham", "Aman", "Aman"} 
print(names) # It dosen't print the repeated values !

data = {"Aman", 5, True, }
print(data)

#  We an apply all the methods which we use in lists as ame 
for n in names : 
    print(names)
    
    
fruits = set()
print(type(fruits))



# -----> Sets methods

set1 = {1, 4, 2, 6, 6, 2}
set2 = {100, 40, 50, 6}

print(set1.union(set2)) #1.---> It merge the two sets

set1.update(set2) #2.---> It update the set
print(set1, set2)


city1 = {"Mumbai", "Lucknow", "Jaipur", "Aurangabad", "Patna"}
city2 = {"Lucknow", "Agra", "Illahabad", "Patna"}

city3 = city1.intersection(city2) #3.---> It return values which is present in the both sets
print(city3)

city1.intersection_update(city2) #4.---> It updates the origin set
print(city1)

cityDiff = city1.symmetric_difference(city2) #5.---> It returns that value which is not common in both sets 
print(cityDiff)

                       
print(city1.isdisjoint(city2)) #6.---> It returns  'true' if the given items are present in another sets other wise 'false'

print(city1.issuperset(city2)) #7.---> It checks if the particular values are already present in the given set or not

city1.add("Srinagar") #8.---> It add a new elelment in the beggining of the list
print(city1)

city1.update(city2) #9.---> It add multiple items in the list

city1.remove("Srinagar") #10.---> It remove a particular element from the list

city1.discard("nice") #11.---> It remove a particular element from the list

print(city1)

popElement = city1.pop() #12.----> It remove the first element from the set
print(popElement)
print(city1)

del city1 #.13---> It delete the entire sets

#---> note: 'remove' method gives an error in the other hand 'discard' method dosen't give an error
