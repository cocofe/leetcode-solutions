
# @Title: N 叉树的前序遍历 (N-ary Tree Preorder Traversal)
# @Author: cocofe
# @Date: 2020-09-30 23:52:24
# @Runtime: 44 ms
# @Memory: 15.4 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        def helper(node):
            if not node:
                return
            ans.append(node.val)
            for child in node.children:
                helper(child)
        helper(root)
        return ans
        
