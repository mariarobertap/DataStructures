#226. Invert Binary Tree - LeetCode

#Link: https://leetcode.com/problems/invert-binary-tree/

#Note: Use DSF algo with a recursive solution to invert the subtrees


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        if(not root):
            return None
        
        
        
        root.left, root.right = root.right, root.left
        
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        
        return root
