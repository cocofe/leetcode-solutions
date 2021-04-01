
# @Title: 两数相加 (Add Two Numbers)
# @Author: cocofe
# @Date: 2018-04-02 21:46:35
# @Runtime: 133 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        idx_1 = idx_2 = 0
        while l1 is not None:
            num1 += 10 ** idx_1 * l1.val
            l1 = l1.next
            idx_1 += 1
        while l2 is not None:
            num2 += 10 ** idx_2 * l2.val
            l2 = l2.next
            idx_2 += 1
        total = num1 + num2
        root = ListNode(total % 10)
        total = total // 10
        current = root
        while total != 0:
            tmp_node = ListNode(total % 10)
            total = total // 10
            current.next = tmp_node
            current = tmp_node
        return root
            
        
