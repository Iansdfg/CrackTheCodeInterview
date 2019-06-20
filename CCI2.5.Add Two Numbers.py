# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = 0
        head = curr = ListNode(0)
        while l1 or l2 or val>0:
            if l1:
                val+=l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next
            newNode = ListNode(val%10)
            curr.next = newNode
            curr = curr.next
            val = val//10
        return head.next
            
        
