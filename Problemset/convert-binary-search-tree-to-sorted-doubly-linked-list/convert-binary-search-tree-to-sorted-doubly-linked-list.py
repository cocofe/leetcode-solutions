
# @Title: 将二叉搜索树转化为排序的双向链表 (Convert Binary Search Tree to Sorted Doubly Linked List)
# @Author: cocofe
# @Date: 2021-03-28 10:50:49
# @Runtime: 60 ms
# @Memory: 14 MB

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
                p = node.right
                while p.left:
                    p = p.left
                p.left = node
                node.right = p
            return right if right else node 
        tail = inorder(root)
        p = tail
        while p.left:
            p = p.left
        tail.right = p
        p.left = tail
        return p

