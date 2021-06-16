# if we want to iterate values from the list which can be possible by forloop
#if we want to get values one by one then we can use for loop
print('Printing values one by one from given list')
x=['Netra',1,34.89,'f']
for item in x:
    print(item)

#here we can get one by one char sequencly
print('Printing char one by one from given string')
y='Netravati'
for i in y:
    print(i)

#it is possible with Set,Tuple or list etc
print('Printing values one by one from given list')
z={'Neeta','Nikhil','Jk','Dhan'}
for i in z:
    print(i)
#Clubbing a two type of collections here by using zip functionality
zip1=zip(z,x)
print(zip1)
for (a,b) in zip1:
    print(a,b)

#how to use range functionality in for loop
print('Printing numbers by mentioning gap')
for i in range(1,10,2):#this is how we can specify the gap while mentioning range
    print(i)

print('printing range in generic case')
for i in range(2,20):#we can just mention range  to be displayed
    print(i)

print('Printing range in reverse')
for i in range(20,11,-1):#this is how we will work with numbers in reverse manner
    print(i)
