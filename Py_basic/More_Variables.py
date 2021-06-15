#here value of num variable is 5
num=5
#num variable has it's own address so how dow get value of address of variable
address_num=id(num)
print(address_num)

#It is possible with all types of variables such as 'str',float,
str='Nik'
address_str=id(str)
print(address_str)

#whenever we create multiple variables with same data then created variables will be pointing to same address_str
a=10
b=a
print(a,b)
print(id(a))
print(id(b))#here both variables are pointing to same same address as they both have same data/values as 10

#here id of the object is considering value of variable not varibale itself.
k=10
print(id(k))

#if we change value of a varibale then we will have differen object and different box
a=9
print(id(a))

#if we change value of a then we don't have different object for b which will point to same value which is 10
print(id(b))

#if we assign a to k variable then both variables are pointing to 9
k=a
print(id(k))

#if we change value of b variable i.e. that will point to 8 values so here all varibales are pointing to different values now instaed 10.So now what will happen to 10 value now.
#now 10 is stored in memory that is unused var
#In python we have garbage collection which will remove unused memory
