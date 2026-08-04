# s="pyThOn"
# print(s.upper())

# p=s.upper()

# print(p)

# print(s.lower())

# a='hellO Java'

# print(a.capitalize())

# c='   hello    '
# print(c,'....')
# print(c.lstrip())
# print(c.rstrip())
# print(c.strip())


# d='apple,banana,hello'
# print(d.split(','))



# e=['banmana','mango','apple']
# print(",".join(e))

# p='H ello '
# print(p.replace(' ',''))


q='He@@l#l@o!&~*?-'
q=q.replace('@','')
q=q.replace('#','')
q=q.replace('!','')
q=q.replace('&','')
q=q.replace('^','')
q=q.replace('*','')
q=q.replace('-','')
q=q.replace('?','')
q=q.replace('~','')

print(q.upper())

q='He@@l#l@o!&~*?-'
i=0
for i in range(len(q)):
    if(q[i] =='@' or q[i] =='#' or q[i] =='!'):
       q = q.replace(q[i],'',1)
    else:
        print(q)
    print()


q = 'He@@l#l@o!&~*?-'
output_q = q

# Loop over each character directly to avoid index errors
for char in q:
    if char == '@' or char == '#' or char == '!' or char =='&' or char =='~' or char =='*' or char =='?' or char =='-':
        # Remove only one instance of the special character from our output
        output_q = output_q.replace(char, '', 1)
    else:
        # Print the current state of the cleaned string
        print(output_q)
    print()

