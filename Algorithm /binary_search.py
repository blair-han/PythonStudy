''' 
Binary search
Binary search works on sorted arrays. 
Binary search begins by comparing an element in the middle of the array with the target value. 
If the target value is greater than the element, the search continues in the upper half of the array.
Logarithmic time
'''

def binary_search(list, item):
    low = 0
    high = len(list)-1
    count = 0

    while low <=high:
        mid = (low + high) // 2
        guess = list[mid]
        count += 1
        print(count)

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) # 1
# print(binary_search(my_list, -1)) # None
