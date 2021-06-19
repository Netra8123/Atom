from array import *
arr=array('i',[])
len=int(input('Please Enter Length of the array '))
for i in range(len):
    x=int(input('Enter the element to be nserted into array '))
    arr.append(x)
print(arr)

search_ele=int(input('Enter element to be searched'))
if search_ele in arr:
    print('present')
else:
    print('Not present')

#If searched item matches one of the values in array then we need to display index of itme
print('Index of searched element by user')
k=0
for item in arr:
    if item==search_ele:
        print(k)
        break;
    k=k+1
