#list  is used store more than one value in the variable
# in other language it is known as array
# list are mutable ie value can be changed inside list

fruits = ['mango','apple','orange','papaya','cherry','watermelon']

print(fruits)

#use len() to count the number of element in list
print(len(fruits)) 

#to access single from the list use indexing 
print(fruits[0]) 

#grab the value of index to and everything after that
print(fruits[2:])

#to add element in the last position of list use append() methods
fruits.append('banana')
print(fruits)

#use pop() to remove element from the list, by default pop remove the last element
# to remove element from the specific position use indexing ie fruits.pop(2) here 2 is a index number

fruits.pop()
print(fruits)

# to remove from specific position
fruits.pop(3) 
print(fruits)

#nesting list -> list inside list
list1 = [2,4,6,8]
list2 = [1,3,5,7]
list3 = [10,15,20,25]

nest_list = [list1,list2,list3]
print(nest_list)

print(list2[2])
print(nest_list[1][2])
