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
        current = head
        while current and current.next:
            if current.next.val == current.val: 
                current.next = current.next.next
            else:
                current = current.next
        return head;
            
        
        
#         arr = []
#         curr = head
#         while curr:
#             if curr.val in arr:
#                 prev.next = curr.next
#             else:
#                 arr.append(curr.val)
#                 prev = curr
#             curr = curr.next
#         return head
