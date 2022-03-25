# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''

URL  = https://leetcode.com/problems/add-two-numbers/


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


'''

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
                
            
            

    
            
          
    
    
        