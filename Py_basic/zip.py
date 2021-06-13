#list zip is used to collect two lists
Name=('Netra','Nikhil')
Company=('Infosys','Accenture')

zipped=list(zip(Name,Company))#Zipped is object where we can store two tuples
print(zipped)

#Set zip is used to collect two lists
Name=('Netra','Nikhil','Netra')
Company=('Infosys','Accenture','Infosys')
#set is unordered and it returns only unique values
zipped=set(zip(Name,Company))#Zipped is object where we can store two tuples
print(zipped)

#Dictionary zip is used to collect two lists
Name=('Netra','Nikhil')
Company=('Infosys','Accenture')

zipped=dict(zip(Name,Company))#Zipped is object where we can store two tuples
print(zipped)

#For loop to retrieve items from the zipped object.
Name=('Netra','Nikhil','Netra')
Company=('Infosys','Accenture','Infosys')

Zipped=zip(Name,Company)
for (a,b) in Zipped:
    print(a,b)
