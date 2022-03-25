
#20. Valid Parentheses

#Link: https://leetcode.com/problems/valid-parentheses/

#Note: Use a hash-map and a stack

#Big O notation: Time O(n): Memory: O(n)

#######################################

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        closeParantheses = {
            ']': '[',
            '}': '{',
            ')': '('
            
        }
        
        for c in s:
            if(c in closeParantheses):
                if(stack and stack[-1] == closeParantheses[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if(not stack):
            return True
        else:
            return False
                
     
        
