'''
map(function name, args)

I can only make the result of map to list once! 
interesting...

>>> python 136.py
1 attempt, calling result list [7, 16, 27, 40, 55]
2 attempt, calling result list []
3 attempt, calling result list []

'''

f = lambda x,y: x*y
x = [1,2,3,4,5]
y = [7,8,9,10,11]

result = map(f,x,y)

# Call the result 3 times.

for i in range(1,4):
	print(f"{i} attempt, calling result list {list(result)}")


