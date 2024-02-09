text = "Hello World"
print(text)

#to count the number of character in a string use len() method
print(len(text))

# string indexing 
print(text[0])

print(text[0:5])
print(text[0:])
print(text[:])

#basic built in string method
#upper()-> uppercase
#lower()-> lowercase
#split()-> split word from the space

print(text.upper())
print(text.lower())
print(text.split())

#formatting with placeholder
print('we are learning %s today at %s' %('python','Dursikshya' ))