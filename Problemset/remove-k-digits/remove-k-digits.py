
# @Title: 移掉K位数字 (Remove K Digits)
# @Author: cocofe
# @Date: 2020-11-15 23:13:43
# @Runtime: 28 ms
# @Memory: 13.1 MB

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        nums = []
        count = k
        for _s in num:
            while nums and k > 0 and nums[-1] > _s:
                nums.pop()
                k -= 1
            nums.append(_s)
        ret = ''.join(nums)
        return ret.lstrip('0')[:len(num)-count] or '0'
        
        
        


            

