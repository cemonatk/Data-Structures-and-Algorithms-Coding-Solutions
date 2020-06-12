def fibonacci(n, result_map={1: 0, 2: 1}):
	if n in result_map:
		return result_map[n]
	else:
		result_map[n] = fibonacci(n-1, result_map) + fibonacci(n-2, result_map) 
		return result_map[n]