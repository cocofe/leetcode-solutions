
# @Title: 递增顺序搜索树 (Increasing Order Search Tree)
# @Author: cocofe
# @Date: 2021-04-25 23:05:11
# @Runtime: 36 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            """
            返回node为根节点, 形成的右子树, 返回head节点
            """
            if not node:
                return
            left = helper(node.left)
            head = left if left else node
            while left and left.right:
                left = left.right
            if left:
                left.right = node
            node.left = None
            right = helper(node.right)
            if right:
                node.right = right
            return head
        return helper(root)

