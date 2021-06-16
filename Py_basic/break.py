x=int(input('How many candies you want '))
i=1
while i<=x:
    print('Candy')
    i=i+1

Available_Can=10
User_wants=int(input('How many candies user wants '))
i=1
while i<=User_wants:
    if i>Available_Can:
        print('Sorry!!!we have limited stock or we have out of stock')
        break;#this is for coming out of block

    print('Candy')
    i=i+1
print('Bye!!!! Have a good Day')
