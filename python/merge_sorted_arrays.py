'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
 
'''

def merge(nums1, m, nums2, n):
    m -= 1
    n -= 1

    index = len(nums1) - 1

    while (index >= 0):

        if (m < 0):
            nums1[index] = nums2[n]
            n -= 1

        elif (n < 0):
            return nums1

        else:
            
            if(nums1[m] > nums2[n]):
                nums1[index] = nums1[m]
                m -= 1
            
            else:
                nums1[index] = nums2[n]
                n -= 1
        index -= 1
    return nums1


nums1 = [1,2,7,0,0,0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))
