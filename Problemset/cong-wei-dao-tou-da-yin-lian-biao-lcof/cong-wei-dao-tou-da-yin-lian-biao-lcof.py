
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: cocofe
# @Date: 2020-05-03 22:29:13
# @Runtime: 24 ms
# @Memory: 15.9 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next
        return stack[::-1]
