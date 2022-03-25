#268. Missing Number

#Link: https://leetcode.com/problems/missing-number/

#Note: sort the array to find the missing num

#Big O notation: Time O(n): Memory: O(1)

#######################################

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        nums.sort()
        
        
        for i in range(len(nums) +1):
            
            if(i == len(nums) and i not in nums):
                return i
            elif(i not in nums):
                return i
