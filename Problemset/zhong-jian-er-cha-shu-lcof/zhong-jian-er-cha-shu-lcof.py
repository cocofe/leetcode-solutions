
# @Title: 重建二叉树 (重建二叉树 LCOF)
# @Author: cocofe
# @Date: 2020-08-17 01:50:15
# @Runtime: 232 ms
# @Memory: 16.9 MB

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
        def helper(pre_idx, start, end):
            if start > end or pre_idx >= len(preorder): return
            print 'root %s, start %s end %s' % (pre_idx, start, end)
            root = TreeNode(preorder[pre_idx])
            p = start
            while inorder[p] != preorder[pre_idx]: p += 1
            root.left = helper(pre_idx + 1, start, p - 1)
            # 前序遍历中跳过左子树的序列(左子树的长度为p - start)
            root.right = helper(p - start + pre_idx + 1, p + 1, end)
            return root
        return helper(0, 0, len(preorder) - 1)
