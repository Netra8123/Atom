#In python we can use for and for else loop together.
#here we just need to print those numbers which are divisible by 5.
nums=[12,15,18,21,25]
for num in nums:
    if num%5==0:
        print(num)
        break;
else:
    print('Not found')

#Here if we mention else statement below if statement then it will print 5 times not found result if required number is not present.
nums=[12,16,18,21,28]
for num in nums:
    if num%5==0:
        print(num)
        break;
else:
    print('Not found')
