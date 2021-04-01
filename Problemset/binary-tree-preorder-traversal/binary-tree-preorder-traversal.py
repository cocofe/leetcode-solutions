
# @Title: 二叉树的前序遍历 (Binary Tree Preorder Traversal)
# @Author: cocofe
# @Date: 2021-02-24 02:28:55
# @Runtime: 20 ms
# @Memory: 12.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], []
        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return ans
            
