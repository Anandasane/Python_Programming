import os

# Writing into the file if file exists and create file when file does not exists

file = open('myfile.text','w')
file.write('hello, java!')
file.close()

# Reading from the file 

file = open('myfile.text','r')
content = file.read()
print(content)
file.close()

# appending the content into the file

# deleting the file 

if os.path.exists('demo.txt'):
    os.remove('demo.txt')
    print('Delete successfully')

else:
    print('file does not exists ')