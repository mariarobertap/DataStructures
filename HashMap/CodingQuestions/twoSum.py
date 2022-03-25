#1. Two Sum

#Link: https://leetcode.com/problems/two-sum/

#Note: use a hash map to store the indices

#Big O notation: Time O(n): Memory: O(n)

#######################################
class Solution(object):

    
    #input [1,2,3,4], target = 6
    
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, value in enumerate(nums):
            key = target - value
            if key in map:
                return [map[key], index]
            else:
                map[value] = index
                    
        
        
