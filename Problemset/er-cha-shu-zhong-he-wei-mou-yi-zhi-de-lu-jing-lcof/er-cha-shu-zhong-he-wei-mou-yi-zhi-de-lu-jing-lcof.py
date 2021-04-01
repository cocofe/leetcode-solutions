
# @Title: 二叉树中和为某一值的路径 (二叉树中和为某一值的路径 LCOF)
# @Author: cocofe
# @Date: 2020-10-25 01:00:44
# @Runtime: 36 ms
# @Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        def track(path, choices):
            # print path, ans, _sum
            if sum(path) == _sum and path and not choices:
                ans.append(path)
                return
            for choice in choices:
                tmp = path[:]
                path.append(choice.val)
                _choices = []
                if choice.left:
                    _choices.append(choice.left)
                if choice.right:
                    _choices.append(choice.right)
                track(path, _choices)
                path = tmp
        if not root: return ans
        track([], [root])
        return ans
