
def divisible(in_list):
	out_list=[]
	for element in in_list:
		if (element % 2 ==0) and (element % 5 == 0):
			out_list.append(element)
	out_list.sort()
	return out_list

my_list = [13,50,-30,3,22,45,100,43]
result = divisible(my_list)
print(result)

