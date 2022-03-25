'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''




def searchRange(self, nums, target):

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