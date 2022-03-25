
#141. linked List Cycle

#Link: https://leetcode.com/problems/linked-list-cycle/

#Note: use a fast pointer and a slow. If they ever met each other, its a cycle

#Big O notation: Time O(n): Memory: O(1)

#######################################


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = head
        fast = head


        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                return True

        return False
