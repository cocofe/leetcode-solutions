
# @Title: 二叉树的最近公共祖先 (二叉树的最近公共祖先 LCOF)
# @Author: cocofe
# @Date: 2020-12-21 21:18:43
# @Runtime: 60 ms
# @Memory: 24.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        if root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not root: return None
        if left is not None and right is not None:
            return root
        elif left is None and right is None:
            return None
        return left if left is not None else right

        
