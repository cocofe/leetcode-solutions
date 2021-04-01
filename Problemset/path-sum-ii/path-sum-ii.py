
# @Title: 路径总和 II (Path Sum II)
# @Author: cocofe
# @Date: 2021-04-01 23:16:41
# @Runtime: 44 ms
# @Memory: 19.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        def helper(node, path, total_sum):
            if not node:
                return
            path.append(node.val)
            if node.left:
                helper(node.left, path[::], total_sum + node.val)
            if node.right:
                helper(node.right, path[::], total_sum + node.val)
            if not node.left and not node.right and total_sum + node.val == targetSum:
                ans.append(path)

        helper(root, [], 0)
        return ans
