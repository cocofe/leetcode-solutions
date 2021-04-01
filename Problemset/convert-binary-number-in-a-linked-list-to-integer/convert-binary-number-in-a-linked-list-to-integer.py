
# @Title: 二进制链表转整数 (Convert Binary Number in a Linked List to Integer)
# @Author: cocofe
# @Date: 2020-01-26 18:10:00
# @Runtime: 20 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        val_set = []
        p = head
        while p:
            val_set.append(p.val)
            p = p.next
        ret = 0
        val_set.reverse()
        for idx, val in enumerate(val_set):
            ret += (val * 2 ** idx)
        return ret
        
