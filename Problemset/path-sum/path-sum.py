
# @Title: 路径总和 (Path Sum)
# @Author: cocofe
# @Date: 2020-08-16 15:21:49
# @Runtime: 24 ms
# @Memory: 16 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, cur_sum):
            if not node:
                return False
            assume_sum = cur_sum + node.val
            is_leaf = not node.left and not node.right
            if is_leaf and assume_sum == sum:
                return True
            cur_sum += node.val
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        return dfs(root, 0)
