
# @Title: 二叉树的坡度 (Binary Tree Tilt)
# @Author: cocofe
# @Date: 2020-10-01 00:21:55
# @Runtime: 52 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            # 返回改节点及所有子节点之和
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)
            self.ans += abs(left - right)
            return left + right + node.val
        helper(root)
        return self.ans
