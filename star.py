num = int(input("Please enter maximum number of stars "))
for x in range(num):
	y = "*"*(x+1)
	print(y)
for x in range(num):
	y = "*"*(num-(x+1))
	print(y)
