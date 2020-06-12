def binarySearch(array, target):
	return driverFunc(array, target, 0, len(array)-1)
	
def driverFunc(array, target, left, right):
	if left > right:
		return -1
	
	middle = (right + left) // 2
	
	if target == array[middle]:
		return middle
	
	elif target < array[middle]:	
		return driverFunc(array, target, left, middle-1)

	else:
		return driverFunc(array, target, middle+1, right)


