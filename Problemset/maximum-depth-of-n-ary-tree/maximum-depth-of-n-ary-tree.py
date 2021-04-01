
# @Title: N 叉树的最大深度 (Maximum Depth of N-ary Tree)
# @Author: cocofe
# @Date: 2020-09-30 23:57:19
# @Runtime: 48 ms
# @Memory: 15.4 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def bfs(node):
            if not node: return 
            return max([bfs(child) for child in node.children if child] or [0]) + 1
        return bfs(root) if root else 0
