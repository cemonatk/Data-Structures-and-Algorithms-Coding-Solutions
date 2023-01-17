"""
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import OrderedDict

        freq_dict = OrderedDict()

        for index, character in enumerate(s):
            if not character in freq_dict:
                freq_dict[character] = [0,index]
            
            else:
                freq_dict[character][0] += 1

        for character, number in freq_dict.items():
            if number[0] == 0:
                print(freq_dict)
                return freq_dict[character][1]
        
        return -1

        



s = "loveleetcode"

print(firstUniqChar(s))
