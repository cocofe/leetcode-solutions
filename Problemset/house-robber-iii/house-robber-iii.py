
# @Title: 打家劫舍 III (House Robber III)
# @Author: cocofe
# @Date: 2021-04-16 00:57:47
# @Runtime: 52 ms
# @Memory: 16.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            ls, ln = helper(node.left)
            rs, rn = helper(node.right)
            return node.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(helper(root))
