#Printing below pattern
# # # #
# # # #
# # # #
# # # #
#First Method
print('# '*4)
print('# '*4)
print('# '*4)
print('# '*4)

#Second Method which prints #*4 in horizantal format
print('# ',end='')
print('# ',end='')
print('# ',end='')
print('# ',end='')
print()

#3rd Method which is very efficient
print('Printing #*4 in very efficient way')
for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()

#The below program is to displa below pic
#
# #
# # #
# # # #
for i in range(4):
    for j in range(i):
        print('# ',end='')
    print()
