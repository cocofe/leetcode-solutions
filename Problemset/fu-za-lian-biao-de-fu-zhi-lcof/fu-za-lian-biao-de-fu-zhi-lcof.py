
# @Title: 复杂链表的复制 (复杂链表的复制  LCOF)
# @Author: cocofe
# @Date: 2020-10-28 22:43:20
# @Runtime: 36 ms
# @Memory: 13.8 MB

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
        # deep copy 链表
        link_map = {}
        p = head
        c_head = Node(-1)
        cp = c_head
        while p:
            node = Node(p.val)
            link_map[p] = node
            cp.next = node
            cp = node
            p = p.next
        p = head
        cp = c_head.next
        while p:
            if p.random:
                cp.random = link_map[p.random]
            p = p.next
            cp = cp.next
        return c_head.next





