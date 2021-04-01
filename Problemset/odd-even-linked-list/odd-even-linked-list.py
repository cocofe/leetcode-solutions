
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: cocofe
# @Date: 2020-11-14 15:44:50
# @Runtime: 36 ms
# @Memory: 16.3 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = ListNode(None)
        even_head = ListNode(None)
        idx = 0
        p = head
        odd_p, even_p = odd_head, even_head
        while p:
            idx += 1
            nex = p.next
            p.next = None
            if idx % 2 == 0:
                even_p.next = p
                even_p = even_p.next
            else:
                odd_p.next = p
                odd_p = odd_p.next
            p = nex
        odd_p.next = even_head.next
        return odd_head.next
                


