# Lists in python
colors = ["red", "green", "blue", "ornage", "pink", "black"]

print(len)
print(colors[1]) # It shows the element with the given index

print(colors[-4]) # first we've to convert it in positive which will '4' then we've to subtract this from the total length of lists which will '6-4 = 2'  and whatever the element is on the result that will be answer which will 'blue'



#---> It shows a particular element exists in list or not 
if "green" in colors :
    print("yes green is available...")
else :
    print("Green is not available...")


# we're appending lists using 'range'
lists = [b for b in range(1,11)] 
print(lists)



#------------> list methods
numbers = [1, 4, 2, 6, 8, 11, 40, 22, 1, 1, 1, 5]
numbers.append(100) #1. It add a new element at the end of the list

numbers.sort() #2. It'll arrange the list in ascending order
numbers.sort(reverse=True) # It'll arrange the list in descending order
numbers.reverse() #3. It'll reverse the list

print(numbers.index(4)) #4. It shows the index of the given element
print(numbers.count(1)) #5. It'll count the number that how many times is  repeated

c =  numbers.copy() #6. It copy the list from the given element
print(c)

numbers.insert(0, 433)  #7. It insert a partcular element in the given index
print(numbers)

colors = ["orange", "blue", "pink"]
numbers.extend(colors) #8. It add a list with the another given list
print(numbers)