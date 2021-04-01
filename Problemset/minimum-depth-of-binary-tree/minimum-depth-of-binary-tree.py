
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: cocofe
# @Date: 2020-09-22 22:16:45
# @Runtime: 32 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = collections.deque()
        if not root: return 0
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
