
# @Title: 二叉树中的最大路径和 (Binary Tree Maximum Path Sum)
# @Author: cocofe
# @Date: 2021-03-17 00:44:51
# @Runtime: 80 ms
# @Memory: 25.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('-inf')]
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            ret = max([node.val + left, node.val + right, node.val, node.val + left + right])  
            ans[0] = max(ans[0], ret)
            return max([node.val + left, node.val + right, node.val])  
        helper(root)
        return ans[0]
