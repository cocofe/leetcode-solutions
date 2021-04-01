
# @Title: 二叉树的层平均值 (Average of Levels in Binary Tree)
# @Author: cocofe
# @Date: 2020-10-01 00:27:18
# @Runtime: 36 ms
# @Memory: 16.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = collections.deque()
        ans = []
        if not root: return ans
        q.append(root)
        while q:
            _sum = 0
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(_sum / float(length))

        return ans
                
