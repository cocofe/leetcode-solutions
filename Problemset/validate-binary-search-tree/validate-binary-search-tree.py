
# @Title: 验证二叉搜索树 (Validate Binary Search Tree)
# @Author: cocofe
# @Date: 2021-03-08 20:20:04
# @Runtime: 36 ms
# @Memory: 17.5 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, mx, mi):
            if not node:
                return True
            if not node.left and not node.right and mi < node.val < mx:
                return True
            if node.left and (node.left.val >= node.val or node.left.val <= mi):
                return False
            if node.right and (node.right.val <= node.val or node.right.val >= mx):
                return False
            return bool(helper(node.left, node.val, mi) and helper(node.right, mx, node.val))
        return helper(root, float('inf'), float('-inf'))

            
