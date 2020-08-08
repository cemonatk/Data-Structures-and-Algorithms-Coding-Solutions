'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Input: "A man, a plan, a canal: Panama"
Output: true
'''

def cleaner(str_input):
    tmp_array = []
    for character in str_input.lower():
        if character.isalnum():
            tmp_array.append(character)
        else:
            pass
    return ''.join(tmp_array)
    
def isPalindrome(string):
    string = cleaner(string)
    lindex = 0
    rindex = len(string) - 1
    while lindex < rindex:
        if string[lindex] != string[rindex]:
            return False
        lindex += 1 
        rindex -= 1
    return True

# true:
print(isPalindrome("aaa!@#$%^&*())x(*&^%$#!aa"))
# false:
print(isPalindrome("aaa!@#$%^&*())(*&^%$#!aa"))


