# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.bfs(root, res, 0)
        for ele in res:
            print(ele.next.val)

    def bfs(self, root, res, depth):
        if root:
            if len(res) == depth:
                res.append(ListNode(-1))
            level = res[depth]
            while level.next:
                level = level.next
            level.next = ListNode(root.val)
            self.bfs(root.left, res, depth + 1)
            self.bfs(root.right, res, depth + 1)
