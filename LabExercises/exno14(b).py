try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")
try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")

