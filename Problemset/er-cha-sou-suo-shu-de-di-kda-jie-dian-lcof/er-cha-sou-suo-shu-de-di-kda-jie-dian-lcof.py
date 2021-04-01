
# @Title: 二叉搜索树的第k大节点 (二叉搜索树的第k大节点  LCOF)
# @Author: cocofe
# @Date: 2020-08-19 13:23:33
# @Runtime: 56 ms
# @Memory: 20.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans[0 - k]
