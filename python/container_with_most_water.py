'''
Source:  https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

my solution:
most water == max of surface calculations 
surface calculations == (x*y) -> where x = difference between indices j-i and y = min(height[i], height[j])


'''
# 2 pointer approach

def maxArea(height: list[int]) -> int:
	max_surface = 0
	
	left = 0
	right = len(height) - 1

	while left < right:
		minimum = min(height[left], height[right])
		max_surface = max((right-left) * minimum, max_surface)

		if height[left]	< height[right]:
			left += 1
		else:
			right -= 1

	return max_surface

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(height))

'''
# naive solution:
def maxArea(height: list[int]) -> int:
	max_surface = 0

	for i in range(len(height)):
		for j in range(i+1, len(height)):
			minimum = min(height[i], height[j])
			max_surface = max((j-i) * minimum, max_surface)	
	return max_surface
'''
