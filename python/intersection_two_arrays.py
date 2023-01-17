class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1_set = set(nums1)
        
        result_array = []

        for value in nums2:
            if value in num1_set and not value in result_array:
                result_array.append(value)
        
        return result_array # return num1_set & set(nums2)
