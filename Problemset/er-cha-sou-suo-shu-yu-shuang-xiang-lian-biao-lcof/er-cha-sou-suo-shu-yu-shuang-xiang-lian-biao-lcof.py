
# @Title: 二叉搜索树与双向链表 (二叉搜索树与双向链表  LCOF)
# @Author: cocofe
# @Date: 2020-08-16 14:02:26
# @Runtime: 64 ms
# @Memory: 13.6 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        def inorder(node):
            if not node or not (node.left or node.right):
                return node
            left = inorder(node.left)
            if left:
                left.right = node
                node.left = left
            right = inorder(node.right)
            if right:
                right.left = node
            return right if right else node 
        tail = inorder(root)
        p = tail
        while p.left:
            p = p.left
        tail.right = p
        p.left = tail
        return p

