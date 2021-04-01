
# @Title: 删除链表中的节点 (Delete Node in a Linked List)
# @Author: cocofe
# @Date: 2020-10-28 22:01:36
# @Runtime: 16 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
