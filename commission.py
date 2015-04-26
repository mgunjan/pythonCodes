
while True:
	sales= float(input("Please enter the total sales amount in USD (-1 to quit):"))
	if (sales <0):
		break
	elif(sales < 10000):
		commission = (.05*sales)
	elif(sales < 20000):
		commission = (.1*sales)
	elif(sales<50000):
		commission = (.15*sales)
	else:
		commission = (.20*sales)
	print("Your commission is :{0:.2f}".format(commission))

