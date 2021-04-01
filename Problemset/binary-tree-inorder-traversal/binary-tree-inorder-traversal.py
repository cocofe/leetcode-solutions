
# @Title: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
# @Author: cocofe
# @Date: 2021-02-23 09:05:43
# @Runtime: 16 ms
# @Memory: 13 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
            

