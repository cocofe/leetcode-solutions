
# @Title: 二叉搜索树中第K小的元素 (Kth Smallest Element in a BST)
# @Author: cocofe
# @Date: 2021-04-10 00:14:19
# @Runtime: 60 ms
# @Memory: 18.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        idx = 0
        ans = None
        def helper(node):
            nonlocal idx, ans
            if not node or ans is not None:
                return
            helper(node.left)
            # 这个idx表示当前元素在有序数组中的位置(中序遍历)
            idx += 1
            if idx == k:
                ans = node.val
                return 
            helper(node.right)
        helper(root)
        return ans
            
