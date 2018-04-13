# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    
    Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
    """
    def nthUglyNumber(self, n):
        """
        # 丑数示例: 1,2,3,4,5,6,8,9,10,12,15, ...
        #       2,   3,      5
        
        # 1,    2,   3,      5
        # 2,    4,   6,      10
        # 3,    6,   9,      15
        # 4,    8,   12,     20
        # 5,    5*2, 5*3,   5*5
        
        实际上下一个丑数是从已有的丑数中分别乘以 2,3,5 所得的最小值中得到的
        初始已有丑数为 1, 下一个可选丑数有 1*2,1*3,1*5 , 因此选择2
        初始已有丑数为 1,2 下一个可选丑数为 2*2, 1*3, 1*5 (注意这里是不考虑2*3,2*5的) ,因此选择 3
        由上面可以找到规律, 设置t2,t3,t5 = 0,0,0 表示下一个*2, *3,*5 的数的索引(*是乘以的意思)
        :type n: int
        :rtype: int
        """
        t2, t3, t5 = 0, 0, 0
        count = 1
        ans = [1]
        while count < n:
            r2, r3, r5 = 2 * ans[t2], 3 * ans[t3], 5 * ans[t5]
            ans_tmp = min(r2, r3, r5)
            if ans_tmp != ans[-1]:
                count += 1
                ans.append(ans_tmp)
            if r2 == ans_tmp:
                t2 += 1
            elif r3 == ans_tmp:
                t3 += 1
            else:
                t5 += 1
        return ans[-1]

    def test(self):
        n = 1600
        print self.nthUglyNumber(n)