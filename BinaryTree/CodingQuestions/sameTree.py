#100. Same Tree - LeetCode

#Link: https://leetcode.com/problems/same-tree/

#Note: Use DSF algo with a recursive solution to compare all the nodes

#Big O notation: Time O(n): Memory: O(1)

##########################################



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        
        if(not p and not q):
            return True
        
        if(not p or not q):
            return False
        
        if(p.val != q.val):
            return False
        
        
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) )
        
        
