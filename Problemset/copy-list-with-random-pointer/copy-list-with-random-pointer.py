
# @Title: 复制带随机指针的链表 (Copy List with Random Pointer)
# @Author: cocofe
# @Date: 2021-03-30 02:03:24
# @Runtime: 48 ms
# @Memory: 13.7 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node_map = {}
        new_head = Node(0)
        p = head
        new_p = new_head
        while p:
            node = Node(p.val)
            node_map[p] = node
            new_p.next = node
            new_p = new_p.next
            p = p.next
        p = head
        while p:
            node = node_map[p]
            ran_node = p.random
            if ran_node:
                node.random = node_map[ran_node]
            p = p.next
        return new_head.next
        

