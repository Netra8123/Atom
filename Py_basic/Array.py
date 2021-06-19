#Array->It includes all values of same data type and it's very flexible to add up iesm if we need.
#if it's int array then all values should be interger dataype
#Advatage here:Array doesn't have fixed and specific size.we can expand size of Array
#For example if we have 5 items in the array if e want to increase items by exending size.I's possible in array.
#If we have 5 itmes then we wan just 4 items from the array then we can shrink it by decreasing the size of the array.
from array import * #It means we need all functions of array here.hence we are importing all functions via *
values=array('i',[2,3,4,5,6])#here everydataype has it's own unique code si we have to use unique code in Array
print(values)

#Specified values using index
print(values[0])
#Reversing
values.reverse()
print(values)

#we can have negative values here as i is signed interger which goes from negative to positive
values_1=array('i',[2,3,4,-1,-5])
print(values_1)

#Details of array
print(values.buffer_info()) #Output will be (2753393269360, 5) here first value is address of Array and 5 is size of teh array
print(values_1.buffer_info())

#We have other methods as well which are called typecode
print(values.typecode) #it prints type of array->i

#We can print iems from array one by one
# for loop go for index values
for i in range(5):
    print(values[i])
#Optimized way to prin values one by one from array
print("Optimized way to print values one by one from array")
for i in range(len(values)):
    print(values[i])

#For loop will directly go for values presented in Array
print('For loop will go to items directly instead index')
for item in values_1:
    print(item)

#how to copy old array values into  a new array
print('Copying values of olde array into a new array')
new_array=array(values.typecode,(a for a in values))#here we are copying same type code from older array to new array and getting value one by one from older array and putting into a new Array
for item in new_array:
    print(item)

#We can work with char items here with Array
values_2=array('u',['a','h','j','k']) #u is unicode  of character
print(values_2.typecode)
print(values_2[2])
for item in values_2:
    print(item)
for i in range(len(values_2)):
    print(values_2[i])

#While loop instead fro loop
i=0
while i<len(values):
    print(values[i])
    i=i+1
