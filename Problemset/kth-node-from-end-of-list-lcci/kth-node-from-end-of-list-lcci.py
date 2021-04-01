
# @Title: 返回倒数第 k 个节点 (Kth Node From End of List LCCI)
# @Author: cocofe
# @Date: 2020-10-26 20:46:19
# @Runtime: 28 ms
# @Memory: 13 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        idx = 1
        p= head
        while p:
            if idx == k:
                break
            idx += 1
            p = p.next
        p2 = head
        while p.next:
            p2 = p2.next
            p = p.next
        return p2.val
