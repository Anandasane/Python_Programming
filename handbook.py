# string and its operations

word = "amazing" 
print(word[1: 6: 2]) # "mzn"

Word = "amazing" 
print(Word[:7])  # word [0:7] – 'amazing' 
print(Word[0:])  # word [0:7] – 'amazing'

print(len(word))
print(word.endswith('ing'))

freq = word.count('a')
print(freq)

cap = word.capitalize()
print(cap)

index = word.find('z')
print(index)

replace = word.replace('z','T')
print(replace)

# EXERCISE

from datetime import datetime

# user= str(input("Enter your name: "))
# print(user,'Good Afternoon')

# current_date = datetime.now().strftime("%B %d, %Y")

# letter = f'''
#     Dear {user},
#     You are selected!
#     Date: {current_date}
# '''
# print(letter)

# text = input("Enter a sentence to check if it contains double space: ")
# if "  " in text:
#     print("❌ Double space detected!")
    
#     # Find the exact index position of the first double space
#     position = text.find("  ")
#     print(f"📍 First double space found at index position: {position}")
# else:
#     print("✅ No double spaces found in the text.")

letter = "Dear Harry, this python course is nice. Thanks!"

# Formatted version using escape sequence characters
formatted_letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

# Print the result
print(formatted_letter)

# List and Tuple

# List
l1 = [7,9,"harry"] 
l1[0] # 7 
l1[1] # 9 
#l1[70]  # error 
l1[0:2] # [7,9]  #list slicing 

l1 = [1,8,7,2,21,15]

# List Methods 

l1.sort() # sort the list in ascending order
print(l1) # [1, 2, 7, 8, 15, 21]
l1.reverse() # reverse the list
l1.append(99) #
l1.insert(2,18) #
l1.pop(3) #
l1.remove(21) #

# tuple in python is immutable, meaning its elements cannot be changed after creation.

a = () # empty tuple 
a = (1,) # tuple with only one element needs a comma 
a = (1,7,2) # tuple with more than one element 

# Tuple Methods
a=(2,3,1,1,4)
print(a.count(1)) # returns number of times 1 occurs
print(a.index(1)) # returns first index when 1 occurs

# EXERCISE

user = list(input("Enter a 7 fruits: "))
print(user)