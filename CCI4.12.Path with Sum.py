# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.findSum(root, sum, [], res)
        return res

    def findSum(self, root, sum, path, res):
        if not root: return
        path.append(root.val)
        if sum == root.val and not root.left and not root.right:
            res.append(path[:])
            return
        self.findSum(root.left, sum - root.val, path[:], res)
        self.findSum(root.right, sum - root.val, path[:], res)
        path.pop()
