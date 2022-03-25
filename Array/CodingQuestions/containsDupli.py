#217. Contains Duplicate

#Link: https://leetcode.com/problems/contains-duplicate/

#Note: Use a hash map to verify if exists

#Big O notation: Time O(n): Memory: O(n)

#######################################


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        numsHash = {}
        
        
        for i in nums:
            if(i in numsHash):
                return True
            else:
                numsHash[i] = 0
                
        return False
