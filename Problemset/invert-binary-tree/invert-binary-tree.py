
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: cocofe
# @Date: 2020-04-01 01:54:34
# @Runtime: 16 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        tmp = root.left
        root.left = right
        root.right = tmp
        return root
