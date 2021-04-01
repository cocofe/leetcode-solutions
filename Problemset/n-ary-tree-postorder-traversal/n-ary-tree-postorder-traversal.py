
# @Title: N 叉树的后序遍历 (N-ary Tree Postorder Traversal)
# @Author: cocofe
# @Date: 2020-09-30 23:52:59
# @Runtime: 44 ms
# @Memory: 15.5 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        def helper(node):
            if not node:
                return
            for child in node.children:
                helper(child)
            ans.append(node.val)
        helper(root)
        return ans
