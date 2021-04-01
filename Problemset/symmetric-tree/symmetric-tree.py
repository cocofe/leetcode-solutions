
# @Title: 对称二叉树 (Symmetric Tree)
# @Author: cocofe
# @Date: 2020-08-13 02:28:29
# @Runtime: 24 ms
# @Memory: 12.5 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def is_same_node(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.is_same_node(left.left, right.right) and self.is_same_node(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        from collections import deque
        q = deque()
        q.append([root.left, root.right])
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            q.append([left.left, right.right])
            q.append([left.right, right.left])
        return True
        # return self.is_same_node(root, root)
        
