
# @Title: 回文链表 (Palindrome Linked List)
# @Author: cocofe
# @Date: 2020-11-02 20:39:12
# @Runtime: 68 ms
# @Memory: 31.6 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        if length <= 1:
            return True
        mid = length / 2 if (length % 2 == 0) else length / 2 + 1
        p = head
        idx = 0
        while p and idx != mid:
            p = p.next
            idx += 1
        prev = None
        while p:
            head_2 = p
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        p1, p2 = head, head_2
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True   
            
