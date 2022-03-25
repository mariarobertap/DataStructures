
#206. Reverse Linked List

#Link: https://leetcode.com/problems/reverse-linked-list/

#Note: reversing a array and adding to the linked list

#Big O notation: Time O(n): Memory: O(1)
#######################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        reversedLL = []
        i = 0
        
        while curr:
            reversedLL.append(curr.val)
            curr = curr.next
            
        reversedLL = reversedLL[::-1]
        curr = head
        while curr:
            curr.val = reversedLL[i]
            curr=curr.next
            i+=1
            
        return head
        
        
