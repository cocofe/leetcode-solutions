
# @Title: 两个链表的第一个公共节点 (两个链表的第一个公共节点  LCOF)
# @Author: cocofe
# @Date: 2020-08-13 00:34:19
# @Runtime: 192 ms
# @Memory: 41.7 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h1, h2 = headA, headB
        while h1 != h2:
            h1 = headB if not h1 else h1.next
            h2 = headA if not h2 else h2.next
        return h1
