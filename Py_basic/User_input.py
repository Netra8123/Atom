#here we go how to get an input from the user
x=input('Enter num1')
y=input('Enter num2')
z=x+y
print(type(z))#here output will be 13 why because whenever we enter number using input() it will be considered as string in python
#hence we are getting result in terms of string we need to convert str format into integer format.

a=input('Enter First Num ')
a1=int(a)
b=input('Enter Second Num ')
b1=int(b)
c=a1+b1
print(c)

#we can directly covert str into int by giving int datatype infrom of input function
h=int(input('Enter Number 1 '))
n=int(input('Enter Number 2'))
m=h+n
print(m)

#how to get char input from user
ch=input('Enter character')
print(ch)#here output will be netra when we entered entire string instead one character.Still this function is taking entire string
#to overcome this problem we can use below stuff
ch1=input('Enter a char')[0]#it will take only one char as 0th index is mentioned
print(ch1)#here output will be one chat even though if we have mentioned multiple chars input function


#how to get expression kind of input from user
result=eval(input('Enter an expr'))
print(result)#here it will evaluate whatever user has input and give the result
