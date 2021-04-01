
# @Title: 二叉树的后序遍历 (Binary Tree Postorder Traversal)
# @Author: cocofe
# @Date: 2021-02-24 02:29:55
# @Runtime: 20 ms
# @Memory: 13.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, stack = [], [root]
        while stack:
            root = stack.pop()
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
            ans.append(root.val)
        ans.reverse()
        return ans
