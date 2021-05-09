
# @Title: 叶子相似的树 (Leaf-Similar Trees)
# @Author: cocofe
# @Date: 2021-05-10 03:10:54
# @Runtime: 40 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root, nums):
            if not root:
                return
            helper(root.left, nums)
            helper(root.right, nums)
            if not root.left and not root.right:
                nums.append(root.val)
        n1, n2 = [], []
        helper(root1, n1)
        helper(root2, n2)
        return n1 == n2
