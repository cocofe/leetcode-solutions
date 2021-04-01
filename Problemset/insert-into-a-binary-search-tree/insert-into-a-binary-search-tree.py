
# @Title: 二叉搜索树中的插入操作 (Insert into a Binary Search Tree)
# @Author: cocofe
# @Date: 2020-09-30 22:57:12
# @Runtime: 132 ms
# @Memory: 16.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 不要求平衡!!!!
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        



