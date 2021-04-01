
# @Title: 相同的树 (Same Tree)
# @Author: cocofe
# @Date: 2020-03-17 23:00:59
# @Runtime: 20 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            if p != q:
                return False
            return True
        if p.val != q.val:
            return False
        ret = self.isSameTree(p.left, q.left)
        if not ret:
            return False
        ret = self.isSameTree(p.right, q.right)
        if not ret:
            return False
        return True
        
