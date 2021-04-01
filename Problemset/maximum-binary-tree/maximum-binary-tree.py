
# @Title: 最大二叉树 (Maximum Binary Tree)
# @Author: cocofe
# @Date: 2020-10-22 00:05:47
# @Runtime: 288 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right: return None
            max_num = max(nums[left:right+1])
            node = TreeNode(max_num)
            idx = nums.index(max_num)
            left = helper(left, idx-1)
            right = helper(idx+1, right)
            node.left = left
            node.right = right
            return node
        return helper(0, len(nums)-1)
            

