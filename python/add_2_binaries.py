'''
Input:  a = "11", b = "1"
Output: "100"
'''

def binary_to_decimal(binary_input):
    result = 0
    for index in range(len(binary_input)):
        reverse_index = len(binary_input)-index-1
        result += int(2**reverse_index * int(binary_input[index]))
    return result

def decimal_to_binary(decimal_input):
    result = ''
    while(decimal_input > 1): 
        kalan = decimal_input % 2
        result += str(kalan)
        decimal_input = decimal_input // 2
    if decimal_input == 1:
        result += '1'
    return result[::-1]


a, b  = "11", "1"

print(decimal_to_binary(binary_to_decimal(a) + binary_to_decimal(b)))