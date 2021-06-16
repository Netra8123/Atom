#If we do not have any code inside if statement then we can pass it via pass keyword
#in order to contine with execution rather than getting error if we don't have any code statement
for i in range(1,10):
    if i%2!=0:
        pass
    else:
        print(i)
print('Bye! have a good day')
