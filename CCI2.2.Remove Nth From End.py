# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        prv = ListNode(-1)
        prv.next = runner  = head
        while n>0:
            runner = runner.next
            n-=1
        if not runner: return head.next
        while runner:
            prv = prv.next
            runner = runner.next
        prv.next = prv.next.next
        return head
            
