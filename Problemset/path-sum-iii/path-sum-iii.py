
# @Title: 路径总和 III (Path Sum III)
# @Author: cocofe
# @Date: 2021-04-01 23:35:27
# @Runtime: 600 ms
# @Memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = [0]
        def calc_sum(node, cur_sum):
            if not node:
                return
            cur_sum += node.val
            if cur_sum == sum:
                ans[0] += 1
            if node.left:
                calc_sum(node.left, cur_sum)
            if node.right:
                calc_sum(node.right, cur_sum)
        def pre_order(node):
            if not node:
                return
            calc_sum(node, 0)
            pre_order(node.left)
            pre_order(node.right)
        pre_order(root)
        return ans[0]
            
