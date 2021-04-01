
# @Title: 有效的完全平方数 (Valid Perfect Square)
# @Author: cocofe
# @Date: 2020-06-08 18:13:49
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            print left, right
            mid = (left + right) // 2 
            if mid ** 2 > num:
                if mid == right:
                    return False
                right = mid
            elif mid ** 2 == num:
                return True
            else:
                if left == mid:
                    return False
                left = mid
        
        return False
            
            
        
