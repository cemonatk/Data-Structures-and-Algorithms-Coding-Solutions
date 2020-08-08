'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly. 
return ord(x) - ord('0')
'''
import sys

def _int(x):
    return ord(x) - ord('0')

def input_validation(character):
    tempory_integer = _int(character)
    if tempory_integer > 9 or tempory_integer < 0:
        return False
    return True

def addStrings(num1, num2) :
    if len(num1) >= 5100 or len(num2) >= 5100 or num1[0] is '0' or num2 [0] is '0':
        sys.exit("INVALID INPUT DETECTED")

    n1 = n2 = 0

    for c in num1:
        if input_validation(c):
            n1 = n1*10 + _int(c)
        else:
            sys.exit("INVALID INPUT DETECTED") 
    for c in num2:
        if input_validation(c):
            n2 = n2*10 + _int(c)
        else:
            sys.exit("INVALID INPUT DETECTED")
    return str(n1+n2)


print(addStrings('123123','1'*5009))




