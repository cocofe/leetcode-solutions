
# @Title: 最大二叉树 II (Maximum Binary Tree II)
# @Author: cocofe
# @Date: 2020-12-21 21:56:59
# @Runtime: 24 ms
# @Memory: 13.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None: return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
