# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.checkBST(root, float('-inf'), float('inf'))

#     def checkBST(self, root, min, max):
#         if not root:return True
#         if root.val>=max or root.val<=min:
#             return False
#         return self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max)
        

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        self.inOrder(root, nodes)
        print(nodes)
        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i - 1]:
                return False
        return True

    def inOrder(self, root, nodes):
        if root:
            self.inOrder(root.left, nodes)
            nodes.append(root.val)
            self.inOrder(root.right, nodes)


def execute():
    sol = Solution()
    n = [2,1,3]
    print(sol.isValidBST(n))


if __name__ == '__main__':
    execute()

