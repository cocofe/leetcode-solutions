
# @Title: 左叶子之和 (Sum of Left Leaves)
# @Author: cocofe
# @Date: 2020-09-30 23:13:19
# @Runtime: 20 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        def dfs(node):
            if not node: return
            is_left_leaf = bool(node.left and not node.left.right and not node.left.left)
            if is_left_leaf:
                ans.append(node.left.val)
            if not is_left_leaf and node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return sum(ans)
