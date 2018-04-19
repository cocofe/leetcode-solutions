# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

    Example:
    For num = 5 you should return [0,1,1,2,1,2].
    
    Follow up:
    
    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

    """
    def countBits(self, num):
        """
        计算0~num,每个元素的二进制中1的个数, 并以数组方式返回 
        :type num: int
        :rtype: List[int]
        """
        # 6 110 = f(3) + 0
        # 5 101 = f(2) + 1
        # 4 100 = f(2) + 0
        # 3 011
        # 2 010
        # 1 001
        # 0 000
        dp = [0] * (num + 1)
        if num <= 0:
            return [0]
        for i in range(1, num + 1):
            dp[i] = dp[i // 2] + i % 2
        return dp
