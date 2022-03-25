#2. Add Two Numbers

#Link: https://leetcode.com/problems/add-two-numbers/

#Note: 

#Big O notation: Time O(n): Memory: O(1)
#######################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carryValue = 0
        
        while l1 or l2 or carryValue:
            
            if(l1):
                v1 = l1.val
            else:
                v1 = 0
            if(l2):
                v2 = l2.val
            else:
                v2 = 0
                
            val = (v1+v2+carryValue)
            if(val >= 10):
                # convert int to string
                val = str(val)

                # get the first digit
                first_digit = val[0]
                carryValue = int(first_digit)
                val = int(val[1])
            else:
                carryValue = 0
                
            cur.next = ListNode(val)
            cur = cur.next
                   
            if(l1):
                l1 = l1.next
            else:
                l1 = None
            
            if(l2):
                l2 = l2.next
            else:
                l2 = None
                
        return dummy.next
                
            
            

    
            
          
    
    
        
