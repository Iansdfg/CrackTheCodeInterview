# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def inorderSuccessor(self, root, p):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :rtype: TreeNode
#         """
#         res = []
#         self.inOrder(self, root, res)
#         for i in range(len(res)):
#             if res[i] == p:
#                 return res[i+1] if i+1 < len(res) else None
#
#
#     def inOrder(self,root, res):
#         if root:
#             self.inOrder(root.left)
#             res.append(root)
#             self.inOrder(root.right)

class Solution(object):
    def inorderSuccessor(self, root, p):
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


