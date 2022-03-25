#199. Binary Tree Right Side View - LeetCode

#Link: https://leetcode.com/problems/binary-tree-right-side-view/

#Note: Use BSF algo to get all the right nodes of each level of the binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        queue  = collections.deque()
        res = []
        
        queue.append(root)
        
        while queue:
            rightSide = None
            queueLen = len(queue)
            
            for i in range(queueLen):
                node = queue.popleft()
                
                if(node):
                    rightSide = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if(rightSide != None):
                res.append(rightSide)
                
        return res
                
                
        
