''' This program showcase Dictionary operation'''

'''Create Dictionary taking user input for 6 persons'''

user_info = {}
for i in range(6):
    name =input('Please enter person {0:d}\'s name: '.format(i+1))
    age = int(input('Please enter person {0:d}\'s age: '.format(i+1)))
    loy_point = int(input('Please enter person {0:d}\'s loyalty points: '.format(i+1)))
    dict1 = {(name):[age,loy_point]}
    user_info.update(dict1)
    
'''Accessing Dictionary and Displaying User info and available Discount'''
i =1
print('\nThe Dictionary contain')
for key,value in user_info.items():
    print('For person {0:d}: name= {1:s}, age = {2:d}, loyalty points={3:d}'.format(i,key,value[0],value[1]))
    i+=1
    if(value[0]>= 65):
        print('Eligible for a senior citizen discount')
    if(value[0]< 12):
        print('Eligible for free kid\'s dessert')
    if(value[1]>= 1000):
        print('Eligible for a free meal')
    elif(value[1]>=500):    
        print('Eligible for a 20% discount')
    elif(value[1]>=100):
        print('Eligible for a 10% discount')
    print('\n')
    
'''End of the program'''
