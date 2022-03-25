'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/


Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''



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
        
        '''
        Input: head = [1,1,2]
        Output: [1,2]
        
        '''
        curr = head
        if head == None:
            return head
        
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    ''']
            if(not head):
            return head
        
 
        curr = head
        
        
        while curr:
        
            if(curr.next):

                if(curr.val == curr.next.val):
                    curr.next = curr.next.next
                    if(curr.next):
                        if(curr.val == curr.next.val):
                              curr.next = curr.next.next

           
            curr = curr.next

        return head
    '''
            
        
    '''

    '''
            
            
            