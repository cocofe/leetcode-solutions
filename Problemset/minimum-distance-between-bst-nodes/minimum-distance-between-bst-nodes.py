
# @Title: 二叉搜索树节点最小距离 (Minimum Distance Between BST Nodes)
# @Author: cocofe
# @Date: 2021-04-13 00:17:15
# @Runtime: 32 ms
# @Memory: 14.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = float('inf')
        prev = None
        def helper(node):
            nonlocal ans, prev
            if not node:
                return
            helper(node.left)
            if prev is not None:
                ans = min(ans, abs(prev.val - node.val))
            prev = node
            helper(node.right)
        helper(root)
        return ans


