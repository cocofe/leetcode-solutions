
# @Title: 平衡二叉树 (Balanced Binary Tree)
# @Author: cocofe
# @Date: 2020-08-17 03:13:40
# @Runtime: 68 ms
# @Memory: 20.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node: return 0
            return max(map(depth, (node.left, node.right))) + 1
        if not root: return True
        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        if not root.left and not root.right:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right)

