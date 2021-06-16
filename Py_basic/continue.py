#If we want to skip 3 if it's divisible by 3 for given range
#Using continue keyword which will skip the specified statement and continue with remaining execution
for i in range(1,10):
    if i%3==0:
        continue;
    print(i)


print('if we want to skip those numbers which are divisible by 3 or 5 from given range of values then we can use OR Operator')
for i in range(1,10):
    if i%3==0 or i%5==0:
        continue;
    print(i)
print('Bye!Have a good day')
