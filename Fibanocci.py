def rec_fibonacci(n):

	
	if n < 0:
		return None
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return rec_fibonacci(n-1) + rec_fibonacci(n-2) 


res = rec_fibonacci(10)
print(res)





