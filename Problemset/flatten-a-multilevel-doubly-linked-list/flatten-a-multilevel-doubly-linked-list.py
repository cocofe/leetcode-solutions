
# @Title: 扁平化多级双向链表 (Flatten a Multilevel Doubly Linked List)
# @Author: cocofe
# @Date: 2020-10-28 21:50:44
# @Runtime: 120 ms
# @Memory: 13.7 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def helper(head):
            p = head
            while p:
                if p.child:
                    nex = p.next
                    p.next = helper(p.child)
                    p.child.prev = p
                    p.child = None
                    while p.next:
                        p = p.next
                    p.next = nex
                    if nex:
                        nex.prev = p
                p = p.next
            return head
        return helper(head)
        
