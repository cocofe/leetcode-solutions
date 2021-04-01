
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: cocofe
# @Date: 2020-10-01 00:41:40
# @Runtime: 72 ms
# @Memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
        elif t1:
            # node = TreeNode(t1.val)
            return t1
        elif t2:
            # node = TreeNode(t2.val)
            return t2
        # t1_left = t1.left if t1 else None
        # t1_right = t1.right if t1 else None
        # t2_left = t2.left if t2 else None
        # t2_right = t2.right if t2 else None
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
