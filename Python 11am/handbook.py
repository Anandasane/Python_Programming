
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

