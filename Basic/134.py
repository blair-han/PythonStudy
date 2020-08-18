'''
eval() function evaluates the specified expression 
'''

while True:
	inp = input("Plase enter any valid python expression you want to excute : ")

	try:
		result = eval(inp)
	except:
		print("your input is not a valid python code!")
		continue
	else:
		print(result)
		break
