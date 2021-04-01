
# @Title: 两数相加 II (Add Two Numbers II)
# @Author: cocofe
# @Date: 2020-03-11 01:14:02
# @Runtime: 68 ms
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
        s1 = []
        s2 = []
        s3 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        len1 = len(s1)
        len2 = len(s2)
        carry = 0
        for i in range(min(len1, len2)):
            v1 = s1.pop()
            v2 = s2.pop()
            remainder = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) / 10
            s3.append(remainder)
        for s in (s1, s2):
            while s:
                val = s.pop()
                remainder = (val +  carry) % 10
                carry = (val + carry) / 10
                s3.append(remainder)
        if carry:
            s3.append(carry)
        head = None
        s3.reverse()
        for val in s3:
            node = ListNode(val)
            if not head:
                head = node
                p = head
            else:
                p.next = node
                p = p.next
        return head
            
            
            
        
