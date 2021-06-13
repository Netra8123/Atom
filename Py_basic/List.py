#List is a collection where we can store different types of data.
#It's mutable means we can change values of list.
#We can append value to the list.
#We can remove speacifed item from the list.
nums=[25,14,36,95,14]
Names=['Nik','Netra,''John','Neeta','Net']
List=[nums,Names] #We can merge two lists at a time
zipped_list=zip(Names,nums)
for (a,b) in zipped_list:
    print(a,b)

print('Merge List is',List)

#Append values to the lists
nums.append(30)#it will append at the end of the lists
print(nums)

#Remove items from the lists
Names.remove('Net')

#Insert values into list on speacifed index
Names.insert(4,'Nisha')
print(Names)

#Pop-it will remove item based on given index
nums.pop(1)
print(nums)

#Pop-here if we don't specify index values then last elemnet which is entered last will get removed from the list.
nums.pop()
print(nums)

#del -if we want to delete multiple items at a time.
del nums[2:]
print(nums)

#extend-here if we want to add multiple items into the list at a time then we can use extend
nums.extend([32,90,48,56])
print(nums)

#inbuilit functionsin which we can perform in python
min(nums)#minimum values
max(nums)#max values
sum(nums)#total values of lists

#Sort function in python(which sorts items of lists)
nums.sort()
print(nums)
