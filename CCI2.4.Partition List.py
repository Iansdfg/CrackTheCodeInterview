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
        smallH = small = ListNode(0)
        bigH = big = ListNode(0)
        while head:
            nextt = head.next
            if head.val<x:
                small.next = head
                small= small.next
            else:
                big.next = head
                big= big.next
            head.next = None
            head = nextt
        small.next = bigH.next
        return smallH.next
        
