
# @Title: K 个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: cocofe
# @Date: 2021-02-24 03:02:33
# @Runtime: 40 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, start, end):
        prev = None
        curr = start
        while curr != end:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        end.next = prev

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        while True:
            start = prev.next
            p = start
            idx = 0
            while idx < k and p:
                end = p
                p = p.next
                idx += 1
            if idx != k:
                return dummy.next
            nex = end.next
            # print start.val, end.val
            self.reverse(start, end)
            prev.next = end
            start.next = nex
            prev = start
        return dummy.next
