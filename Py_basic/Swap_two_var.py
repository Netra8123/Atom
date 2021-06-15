#how to swap two varibales
a=5
b=6
#For swapping variable we would need temp varibale to store 3rd value
temp=a
a=b
b= temp
print(a,b)

#we can use it in better way instaed third varibale,we have amazing technique in python instaed of using hird variable
a,b=b,a
print(a)
print(b)
#it works as stack basically it works in one line not in two different lines
#Normally pythong solves on right side like b=6 and a=5 it will go to stack and w ehave concept of rotational so hese items will reverse here
#ROT_TWO()-swalps two top most stack items
#it uses concept of two rotational here
