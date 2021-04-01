
# @Title: 删除链表的节点 (删除链表的节点 LCOF)
# @Author: cocofe
# @Date: 2020-08-13 12:24:50
# @Runtime: 24 ms
# @Memory: 13 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        prev = None
        while p:
            if p.val == val:
                if not prev:
                    return p.next
                prev.next = p.next
                p = prev.next
            else:
                prev = p
                p = p.next
        return head

