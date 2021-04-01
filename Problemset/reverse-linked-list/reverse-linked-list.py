
# @Title: 反转链表 (Reverse Linked List)
# @Author: cocofe
# @Date: 2020-11-07 01:00:52
# @Runtime: 28 ms
# @Memory: 19.2 MB

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
        if not head: return head
        lenght = 0
        p = head
        while p:
            lenght += 1
            p = p.next
        succesor = []
        def reverseN(node, n):
            """
            用递归反转0到N的链表
            """
            if n == 1:
                succesor.append(node.next)
                return node
            last = reverseN(node.next, n - 1)
            node.next.next = node
            node.next = succesor[0]
            return last
        return reverseN(head, lenght)
