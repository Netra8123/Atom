#None -datatype
#if we have varibale that is not assigned to any value then we may use null keyword in other languages
#however we use non keyword in python

#Numeric -datatype
#we have multiple types of Numeric like int,float,complex,bool
num=5
print(type(num))

num_float=2.5
print(type(num_float))

#coverting float datatype into integer
convert_ty=int(num_float)
print(convert_ty)

#complexa
num_complex=6+9j
print(type(num_complex))

a=5.6
b=int(a)
print(type(b))

#coverting values into complex types
k=9
c=complex(b,k)
print(c)

#boolen -datatype
#decision making will happen over True and False
bool=b<k
print(bool)
print(type(bool))

#We can convert bool type into integer
print(int(True))
print(int(False))

#Datatypes are none,Numeric,List,Tuple,Set,String,Range,Dictionary
#List
lst=[23,45,67,78]
print(lst)
print(type(lst))

#Set
s={23,36,57,78}
print(s)
print(type(s))

#Tuple
t=(34,45,67,89)
print(t)
print(type(t))

#Dictionary
#when w ehave huge amount of data then we can fetch data in efficient way then we can use dictionary
dict={1:'khk',2:'gs',3:'bvb'}
print(dict)
print(type(dict))

#Range
#if we want to iterate between values then we can use range in python
print(range(10))
#how to covert range into List
print(list(range(10)))
print(type(range(10)))
print(list(range(2,10,2)))#2 to 10 is range and 3rd parameter is difference


#String
str='netra'#double and single quote will owork here
h='a'
print(type(str))
print(type(h))
