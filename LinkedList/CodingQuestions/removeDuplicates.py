#83. Remove Duplicates from Sorted List

#Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

#Note: compare the curr element with the next to decide if the pointer is going to move

#Big O notation: Time O(n): Memory: O(1)

##########################################


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        curr = head
        
        while curr and curr.next:
            
            if(curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head
        
