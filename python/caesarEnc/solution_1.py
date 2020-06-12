def caesarEnc(string, key):
	result = ""
	key %= 26
	
	for char in string:
		new_num = ord(char)+key
		
		if new_num <= 122:
			result += chr(new_num)

		else:
			result +=  chr((new_num % 122) + 96)
	
	return result