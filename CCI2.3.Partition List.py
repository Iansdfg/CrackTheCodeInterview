# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return head
        smallH = small = ListNode(0)
        bigH = big = ListNode(0)
        while head:
            if head.val<x:
                nextt = ListNode(head.val)
                small.next = nextt
                small = small.next
            else:
                nextt = ListNode(head.val)
                big.next = nextt
                big = big.next
            head = head.next
        small.next = bigH.next
        return smallH.next
