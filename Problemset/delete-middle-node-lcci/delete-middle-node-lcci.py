
# @Title: 删除中间节点 (Delete Middle Node LCCI)
# @Author: cocofe
# @Date: 2020-10-29 19:11:39
# @Runtime: 8 ms
# @Memory: 13.1 MB

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
