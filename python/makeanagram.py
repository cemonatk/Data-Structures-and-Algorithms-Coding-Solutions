
"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Sample Input
cde
abc
Sample Output
4
"""


def makeAnagram(a, b):
    # Write your code here
    freq_dict = dict()
    for letter in a:
        if letter not in freq_dict:
            freq_dict[letter] = 0
        freq_dict[letter] += 1

    for letter in b:
        if letter not in freq_dict:
            freq_dict[letter] = 0
        freq_dict[letter] -= 1

    return sum(abs(i) for i in freq_dict.values())
