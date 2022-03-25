#26. Remove Duplicates from Sorted Array

#Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#Note: 

#Big O notation: Time O(n): Memory: O(1)

#######################################

class Solution(object):
    def removeDuplicates(self, nums):
        
        k = 0

        for i in range(len(nums)):
    
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
                

        return k+1
        

                    
                    
                    
                
