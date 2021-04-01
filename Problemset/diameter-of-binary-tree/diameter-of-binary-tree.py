
# @Title: 二叉树的直径 (Diameter of Binary Tree)
# @Author: cocofe
# @Date: 2020-03-31 23:34:50
# @Runtime: 24 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        
        depth(root)
        return self.ans
        
