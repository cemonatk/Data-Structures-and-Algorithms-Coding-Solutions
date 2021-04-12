'''
Source: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''

def raindrop_counter(rain_array):
    left_max, right_max, total_water = 0, 0, 0
    right_pointer, left_pointer = len(rain_array) - 1, 0

    while left_pointer < right_pointer:
        if rain_array[left_pointer] < rain_array[right_pointer]:
            if left_max <= rain_array[left_pointer]:
                left_max = rain_array[left_pointer]
            else:
                total_water += left_max - rain_array[left_pointer]
            left_pointer += 1
        else:
            if right_max <= rain_array[right_pointer]:
                right_max = rain_array[right_pointer]
            else:
                total_water += right_max - rain_array[right_pointer]
            right_pointer -= 1

    return total_water

rain_array = [4,2,0,3,2,5]

print(raindrop_counter(rain_array))

# write test and validation for constraints.
assert (raindrop_counter([4,2,0,-1,2,5]) == 9),"negative value error"
