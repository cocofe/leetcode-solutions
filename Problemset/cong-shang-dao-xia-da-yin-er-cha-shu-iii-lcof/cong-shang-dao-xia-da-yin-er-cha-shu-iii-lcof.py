
# @Title: 从上到下打印二叉树 III (从上到下打印二叉树 III LCOF)
# @Author: cocofe
# @Date: 2021-04-02 00:59:47
# @Runtime: 16 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse = 0
        q = collections.deque()
        ans = []
        if not root:
            return ans
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                level.reverse()
            ans.append(level)
            reverse = not reverse
        return ans
