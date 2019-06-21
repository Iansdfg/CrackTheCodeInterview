# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(arrary):
    if len(arrary) == 0:
        return None
    root = ListNode(arrary[0])
    result = root
    for index, value in enumerate(arrary):
        if index > 0:
            root.next = ListNode(value)
            root = root.next
    return result

def printList(linkedlist):
    if linkedlist:
        print('[', end = '')
        while linkedlist.next:
            print(linkedlist.val, end = ', ')
            linkedlist = linkedlist.next
        print(linkedlist.val, end = ']\n')
    else:
        print('[]')

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:return True
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        if slow.next and prev.val == slow.next.val:
            slow = slow.next
        while prev and slow and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        return not prev and not slow


def execute():
    l1 = initList([1,2,2,2,1])
    sol = Solution()
    print(sol.isPalindrome(l1))

if __name__ == '__main__':
    execute()

