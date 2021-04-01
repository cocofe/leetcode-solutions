
# @Title: 二叉搜索树节点最小距离 (Minimum Distance Between BST Nodes)
# @Author: cocofe
# @Date: 2021-03-31 22:46:09
# @Runtime: 24 ms
# @Memory: 13.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('inf')]
        prev = [None]
        items = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            if prev[0] is not None:
                # print prev, node.val
                ans[0] = min(ans[0], node.val - prev[0])
            prev[0] = node.val
            items.append(prev[0])
            helper(node.right)
        helper(root)
        return ans[0]
