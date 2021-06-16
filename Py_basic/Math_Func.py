#Importing mathematical functions
import math as m
x=m.sqrt(25)
print(x)

#If we want to round of values/integers
#We have a couple of functions in order to round off of values
#when we apply floor function for this 2.9 then result will be 2
#when we apply ceil function for this 2.5 then result willbe 3
y=m.floor(2.9)
print(y)
z=m.ceil(2.5)
print(z)
a=m.ceil(2.1)
print(a)

#pow function to get multiplied number for given value
print(m.pow(2,2))

#value of PI and Epsilon
print(m.pi)
print(m.e)

#after importing if we want to use 'm' instead of using math function
#while performing mathematical functions
#We can use alias name instaed of math functions
b=m.sqrt(25)
print(b)
#Note: wif we put alias name for math function then we need to use alias name to perform mathematical functions
#or else it will throw up an error as "math" is not defined
