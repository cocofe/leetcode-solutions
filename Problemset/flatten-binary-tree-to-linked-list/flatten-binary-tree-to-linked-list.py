
# @Title: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# @Author: cocofe
# @Date: 2020-10-21 23:43:23
# @Runtime: 32 ms
# @Memory: 14.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        left, right = root.left, root.right
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right

        

