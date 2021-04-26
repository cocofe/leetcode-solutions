
# @Title: 二叉搜索树的范围和 (Range Sum of BST)
# @Author: cocofe
# @Date: 2021-04-27 00:31:31
# @Runtime: 296 ms
# @Memory: 23 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return
            helper(node.left)
            if low <= node.val <= high:
                ans += node.val
            helper(node.right)
        helper(root)
        return ans
