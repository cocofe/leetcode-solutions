
# @Title: 把二叉搜索树转换为累加树 (Convert BST to Greater Tree)
# @Author: cocofe
# @Date: 2021-04-29 02:42:02
# @Runtime: 72 ms
# @Memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        _sum = 0
        def helper(node):
            nonlocal _sum
            if not node:
                return
            helper(node.right)
            _sum += node.val
            node.val = _sum
            helper(node.left)
        helper(root)
        return root
