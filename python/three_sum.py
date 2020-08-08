
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array) - 2):
        lindex = i + 1 
        rindex = len(array) - 1
        
        while lindex < rindex:  
            currentSum = array[i] + array[lindex] + array[rindex]
            
            if currentSum == targetSum:
                result.append([array[i]], array[lindex], array[rindex]])
                lindex += 1
                rindex -= 1
            elif currentSum < targetSum:
                lindex += 1
            
            elif currentSum > targetSum:
                rindex -= 1
                
    return result