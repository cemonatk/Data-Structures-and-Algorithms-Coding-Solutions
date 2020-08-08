def selectionSort(array):
	for step in range(len(array)):
		tmp_min = step
		
		for i in range(step+1, len(array)):
			if array[i] < array[tmp_min]:
				tmp_min = i

		(array[step], array[tmp_min]) = (array[tmp_min], array[step])
		
	return array