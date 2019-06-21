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
        s1,s2 = '',''
        while l1:
            s1+=str(l1.val)
            l1 = l1.next
        while l2:
            s2+=str(l2.val)
            l2 = l2.next
        res = str(int(s1)+int(s2))
        head = curr = ListNode(int(res[0]))
        for ele in res[1:]:
            nextt = ListNode(int(ele))
            curr.next = nextt
            curr = curr.next
        return head
            
                
