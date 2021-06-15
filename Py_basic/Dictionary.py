#Key should be immutable and unique
Data={1:'Netr',2:'Nik',3:'Nikhil'}
print(Data)
#If we want to fetch specified value then we can use key.
print(Data[1])

print(Data.get(3))
print(Data.get(4))#If key is not found in the Dictionary then it will give us "None"
#If key is not found in Dict then if we want to print message as "Not found" we can do it
print(Data.get(4,'Not Found'))

print(Data.get(3,'Not Found'))#If key is present in Dict

#If we have two sets of list then we need to merge and convert it into Dictionary.(we can merge two lists into Dictionary)
Keys=['Nikhil','Netra','John','Nik']
Values=['SAP','Python','JS','Java']
Dict=dict(zip(Keys,Values))
print(Dict)

#We can add values into the Dict
Dict['Neeta']='DS'
print(Dict)

#We can remove items from Dictionary
del Dict['Netra']
print(Dict)

#We are trying to list into Dictionary and Dictionary inside Dictionary
prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog['Python'])
print(prog['Python'][0])#It will fetch 0th value of Python key

#We can retrive value of 'Java' and specified value of Dictionary inside the dict
print(prog['Java'])
print(prog['Java']['JSE'])
