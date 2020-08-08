def isValidSubsequence(array, sequence):
	array_index, seq_index = 0, 0
	
	while array_index < len(array) and seq_index < len(sequence):
		if array[array_index] == sequence[seq_index]:
			seq_index += 1
		array_index += 1
	return seq_index == len(sequence)