'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

def isBadVersion(version):
    if version >= 16:
        return True
    else:
        return False 

def firstBadVersion(last, first=1):
   
    last = n

    while first < last:
        middle = (first+last) // 2 
        # middle = first+(last-first)/2

        if (isBadVersion(middle)):
             last = middle 
        else:
            first = middle + 1

    return first

print(firstBadVersion(n))

# n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
