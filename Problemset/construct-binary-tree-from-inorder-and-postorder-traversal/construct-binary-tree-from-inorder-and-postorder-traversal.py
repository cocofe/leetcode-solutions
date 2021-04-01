
# @Title: 从中序与后序遍历序列构造二叉树 (Construct Binary Tree from Inorder and Postorder Traversal)
# @Author: cocofe
# @Date: 2021-03-28 10:20:17
# @Runtime: 388 ms
# @Memory: 17.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(post_idx, st, et):
            if post_idx < 0 or st > et or post_idx >= len(postorder):
                return
            # print post_idx, st, et
            root = TreeNode(postorder[post_idx])
            p = st
            while p < len(inorder) and inorder[p] != postorder[post_idx]:
                p += 1
            # print p
            root.left = helper(post_idx - (et - p + 1), st, p - 1)
            root.right = helper(post_idx-1, p+1, et)
            return root
        return helper(len(postorder)-1, 0, len(inorder) - 1)

