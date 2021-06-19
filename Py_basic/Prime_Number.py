#To check given number is prime or # NOTE:
#What is prime->number which is not divisible by any number that value is considered as "Prime"
#Let's start with 7 number which is prime itself
num=7
for item in range(2,num):#it will take 2 to 6th number
    if num%item==0:
        print("Not Prime Number")
else:
    print("Prime Number")
