
# @Title: 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
# @Author: cocofe
# @Date: 2021-04-01 23:27:35
# @Runtime: 72 ms
# @Memory: 26.5 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        对于一个node节点
        - p,q分别在node节点的左右两侧
        - p, q 在node节点的同一侧
        - p, q 不在node节点的左右侧
        """
        def helper(node):
            if not node:
                return None
            if node == q or node == p:
                return node
            left = helper(node.left)
            right = helper(node.right)
            if left and right:
                return node
            return left or right or None
        return helper(root)

            
        
