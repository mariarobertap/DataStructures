#53. Maximum Subarray

#Link: hhttps://leetcode.com/problems/maximum-subarray/

#Note: if sum start to go down, reset the variable

#Big O notation: Time O(n): Memory: O(n)

#######################################

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum = 0
        res = None
         
        for i in nums:
            
            if(maxSum < 0):
                maxSum = 0
            
            maxSum += i
            
            res = max(maxSum, res)
            
            
        return res
                
        
