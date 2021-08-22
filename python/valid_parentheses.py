'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	if len(s) == 0 or len(s) > 104:
		return False

	hashmap = {
		')':'(',
		'}':'{',
		']':'['
	}
	stack = []
	for character in s:
		if character in hashmap:	
			if stack and hashmap[character] == stack[-1]: # peek
				stack.pop()
			else:
				return False
		else:
			stack.append(character)
	return len(stack) == 0

s = "([)]"
print(isValid(s))
