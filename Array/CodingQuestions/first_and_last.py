#. 34. Find First and Last Position of Element in Sorted Array

#Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#Note: store the first time and last

#Big O notation: Time O(n): Memory: O(1)

#######################################

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        firstPosition = None
        lastPosition = None

        for i in range(len(nums)):
            
            if(nums[i] == target and firstPosition == None):
                firstPosition = i
            if(nums[i] == target and i > lastPosition):
                lastPosition = i
                
        
        if(firstPosition == None and lastPosition == None):
            return [-1,-1]
      
        
        return [firstPosition, lastPosition]
                
        
        
        
        
        
        
