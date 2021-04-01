
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: cocofe
# @Date: 2020-08-13 02:32:54
# @Runtime: 40 ms
# @Memory: 15.1 MB

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
        depth = 0
        if not root:
            return depth
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
