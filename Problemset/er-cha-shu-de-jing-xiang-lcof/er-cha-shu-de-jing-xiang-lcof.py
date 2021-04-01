
# @Title: 二叉树的镜像 (二叉树的镜像  LCOF)
# @Author: cocofe
# @Date: 2020-08-17 00:47:53
# @Runtime: 28 ms
# @Memory: 12.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node: return
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            node.left, node.right = node.right, node.left
        helper(root)
        return root
