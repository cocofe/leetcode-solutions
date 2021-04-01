
# @Title: 二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)
# @Author: cocofe
# @Date: 2020-10-01 00:48:41
# @Runtime: 52 ms
# @Memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        seq = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            seq.append(node.val)
            inorder(node.right)
        inorder(root)
        curr, nex = 0, 1
        ans = None
        while nex < len(seq):
            diff = abs(seq[curr] - seq[nex])
            ans = diff if ans is None else min(ans, diff)
            curr += 1
            nex += 1
        return ans
            
