x='is'
y='my'
z='name'

c=y+ " " +z+ " " +x
print(c)

#Another Method to print
Name='Netra'
Name_1='Nik'
str='My Name is'
res='My Name is {}'.format(Name)
print(res)

res_1='My Name is {}'.format(Name_1)
print(res_1)

#When we have more than one input,then how to print
Gender='Female'
Age=24
Name_3='Netravati'
res_3='My name is {2} and my age is {1} and Gender is {0}'.format(Gender,Age,Name_3)
print(res_3)

# Another Method
Age=25
Name_4='Nikhil'
Res_4=f'My Name is {Name_4} and My Age is {Age}'
print(Res_4)
