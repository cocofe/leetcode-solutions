
# @Title: 二叉树的堂兄弟节点 (Cousins in Binary Tree)
# @Author: cocofe
# @Date: 2021-05-17 22:14:36
# @Runtime: 60 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def helper(node, x, cnt):
            if not node:
                return None
            if (node.left and node.left.val == x) or (node.right and node.right.val == x):
                return node, cnt
            return helper(node.left, x, cnt+1) or helper(node.right, x, cnt+1)
        r1 = helper(root, x, 0)
        r2 = helper(root, y, 0)
        if not all([r1, r2]):
            return False
        p1, c1 = r1
        p2, c2 = r2
        return p1 != p2 and c1 == c2
