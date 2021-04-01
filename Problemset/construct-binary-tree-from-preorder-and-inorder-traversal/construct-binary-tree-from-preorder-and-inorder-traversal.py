
# @Title: 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
# @Author: cocofe
# @Date: 2020-04-02 00:11:53
# @Runtime: 180 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        left_in = inorder[0:idx]
        right_in = inorder[idx+1:]
        root.left = self.buildTree(preorder[1:1 + len(left_in)], left_in)
        root.right = self.buildTree(preorder[1 + len(left_in):], right_in)
        return root
        
