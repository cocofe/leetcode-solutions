
# @Title: 环形链表 II (Linked List Cycle II)
# @Author: cocofe
# @Date: 2020-10-30 00:05:33
# @Runtime: 32 ms
# @Memory: 19.1 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        p = head
        double_p = head.next
        is_cycle = False
        while p and double_p:
            if p == double_p:
                is_cycle = True
                break
            p = p.next
            double_p = double_p.next
            if not double_p:
                return None
            double_p = double_p.next
        if not is_cycle:
            return None
        # 计算环长
        cycle_len = 1
        start = p
        p = p.next
        while start != p:
            cycle_len += 1
            p = p.next
        idx = 0
        curr = head
        count = cycle_len
        nex = head
        while count > 1:
            nex = nex.next
            count -= 1
        while nex.next != curr:
            idx += 1
            nex = nex.next
            curr = curr.next
        return curr
