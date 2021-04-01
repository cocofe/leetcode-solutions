
# @Title: 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
# @Author: cocofe
# @Date: 2020-11-03 23:46:16
# @Runtime: 24 ms
# @Memory: 13 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        prev_head = ListNode(None)
        prev_head.next = head
        count = length - n
        p = prev_head
        while count > 0:
            p = p.next
            count -= 1
        nex = p.next
        p.next = nex.next
        return prev_head.next
