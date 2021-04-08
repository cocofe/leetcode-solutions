
# @Title: 对称的二叉树 (对称的二叉树  LCOF)
# @Author: cocofe
# @Date: 2021-04-09 01:29:13
# @Runtime: 44 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node_1, node_2):
            if not node_1 and not node_2:
                return True
            if not all([node_1, node_2]):
                return False
            if node_1.val != node_2.val:
                return False
            return helper(node_1.left, node_2.right) and helper(node_1.right, node_2.left)
        if not root or (not root.left and not root.right):
            return True
        return helper(root.left, root.right)
            
            
