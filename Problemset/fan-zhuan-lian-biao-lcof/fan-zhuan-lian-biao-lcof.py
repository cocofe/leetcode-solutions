
# @Title: 反转链表 (反转链表 LCOF)
# @Author: cocofe
# @Date: 2020-11-07 00:25:49
# @Runtime: 28 ms
# @Memory: 18 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
