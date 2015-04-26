
def create_tuple(list1,list2,num):
	if( len(list1) < num or len(list2) < num):
		return None
	list_out = []	
	for x in range(num):
		list_out.append((list1[x],list2[x]))
	return tuple(list_out)

list1=['apple','pear','banana','coconut','orange']
list2=[1,2,3,4,5,6,7,8]
num =3
result = create_tuple(list1,list2,num)
print(result)


