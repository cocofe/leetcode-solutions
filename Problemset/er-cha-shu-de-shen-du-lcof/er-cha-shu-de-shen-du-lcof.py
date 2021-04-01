
# @Title: 二叉树的深度 (二叉树的深度 LCOF)
# @Author: cocofe
# @Date: 2020-08-13 12:05:11
# @Runtime: 36 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
