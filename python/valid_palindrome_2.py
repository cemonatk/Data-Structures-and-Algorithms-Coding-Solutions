'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
isalpha()

'''
def cleaner(str_input):
    tmp_array = []
    for character in str_input.lower():
        if character.isalpha():
            tmp_array.append(character)
        else:
            pass
    return ''.join(tmp_array)

def isPalindrome(string):
    if len(string) == 0:
        return False
    string = cleaner(string)

    lindex = 0
    rindex = len(string) - 1
    allowance = 1

    while lindex < rindex:
        if string[lindex] != string[rindex]:
            if allowance == 0:
                return False
            allowance -= 1

        lindex += 1 
        rindex -= 1
        
    return True
    
# true:
print(isPalindrome("abbcba"))
# true:
print(isPalindrome("aba"))