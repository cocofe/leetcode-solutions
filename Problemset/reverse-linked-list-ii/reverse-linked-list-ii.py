
# @Title: 反转链表 II (Reverse Linked List II)
# @Author: cocofe
# @Date: 2021-03-18 01:02:11
# @Runtime: 16 ms
# @Memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    successor = None
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = self.successor
            return last
        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
