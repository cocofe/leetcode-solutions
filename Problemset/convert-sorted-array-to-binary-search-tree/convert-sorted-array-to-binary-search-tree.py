
# @Title: 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)
# @Author: cocofe
# @Date: 2020-08-16 23:32:55
# @Runtime: 32 ms
# @Memory: 17.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(start, end):
            if start > end: return
            mid = (start + end) / 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        return helper(0, len(nums)-1)

