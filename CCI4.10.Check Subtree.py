# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# class Solution(object):
#     def isSubtree(self, s, t):
#         """
#         :type s: TreeNode
#         :type t: TreeNode
#         :rtype: bool
#         """
#         if not s or not t: return not s and not t
#         if self.check(s, t):
#             return True
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

#     def check(self, s, t):
#         if not s or not t: return not s and not t
#         if s.val != t.val:
#             return False
#         return self.check(s.left, t.left) and self.check(s.right, t.right)

        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        Sres,Tres = [],[]
        self.inorder(s,Sres)
        self.inorder(t,Tres)
        print(Sres, Tres)
        for i in range(len(Sres)):
            if Sres[i:i+len(Tres)] == Tres:
                return True
        return False
            
        
    def inorder(self, root,res):
        if not root:
            res.append(None)
        else:
            self.inorder(root.left,res)
            self.inorder(root.right,res)
            res.append(root.val)
        
