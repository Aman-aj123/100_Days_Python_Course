str1 = 'I am in single code'
str2 = "I am in Double code"

 
 #-------> Strings are immutable
 
 
 #-------> Strings Methods 
 
name = "AmaN Raz #"
print(name[0: 5]) # I twill Slice the characters from zero to four
print(len(name))  # Use to print the total length of the string

print(name.upper()) # print the character in 'Uppercase'
print(name.lower()) # print the character in 'Lowercase'
print(name.rstrip("#")) # It removes a particular character from the string
print(name.replace("A", "R")) # It replace a particular character 
print(name.split(" ")) # It will split the string with the given character and return an array
print(name.capitalize()) # It is used to Capitalize the string
print(name.center(25)) # It center the string with the given margin
print(name.count("a")) # It will count the number of characters repeated in string
print(("My name is Aman. I am a good boy.").find("is")) # It will find the index of the first occurence in the string
print(name.isalnum()) # It will return if 'true' if the string is 'alpha numeric' otherwise 'false'
print(name.isalpha())
print(name.islower()) # If the uppercase letter or any other letter is present other than lowercase it will return false

paragraph = "Ram is a good boy \n he is 18 years old"
print(paragraph.isprintable()) # If the character is printable it will return true otherwise false
print(name.isspace()) #If the space is present it will return true otherwise false
print(paragraph.istitle()) # It identifies that the character is a title or not
print(paragraph.title()) # It 'capitalize' the first letter of each word