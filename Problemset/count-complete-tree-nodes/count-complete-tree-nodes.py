
# @Title: 完全二叉树的节点个数 (Count Complete Tree Nodes)
# @Author: cocofe
# @Date: 2020-11-24 21:43:55
# @Runtime: 112 ms
# @Memory: 20.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
