
# @Title: 丑数 II (Ugly Number II)
# @Author: cocofe
# @Date: 2018-04-12 16:03:54
# @Runtime: 321 ms
# @Memory: N/A

class Solution(object):
    def nthUglyNumber(self, n):
        """
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
        
        
        
        
        
        
