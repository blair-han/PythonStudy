'''
filter(function name, instance_list)

list function works only once with list filter function. 
interesting....

>>>python 71.py
1 attempt: the result is [113, 11113, 11119]
2 attempt: the result is []
3 attempt: the result is []

'''


def getPrime(x):
	for i in range(2,x-1):
		if x%i == 0:
			break
	else:
		return x

listdata = [117,119,113,11113,11119]

ret = filter(getPrime, listdata)

for i in range(1,4):
	print(f"{i} attempt: the result is {list(ret)}")
