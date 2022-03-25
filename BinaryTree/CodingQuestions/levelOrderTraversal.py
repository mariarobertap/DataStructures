#102. Binary Tree Level Order Traversal - LeetCode

#Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
#Note: Use BSF algo to get all the nodes of each level of the binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res =[]
        queue = collections.deque()
        queue.append(root)
        
        
        while queue:
            
            queueLen = len(queue)
            level = []
            for i in range(queueLen):
                node = queue.popleft()
                
                if(node):
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if(level):
                res.append(level)
                
                
        return res
            
            
