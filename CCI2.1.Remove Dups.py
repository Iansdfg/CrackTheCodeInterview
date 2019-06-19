# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        curr = head
        while curr:
            if curr.val in arr:
                prev.next = curr.next
            else:
                arr.append(curr.val)
                prev = curr
            curr = curr.next
        return head
