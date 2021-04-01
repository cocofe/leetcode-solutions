
# @Title: 分割平衡字符串 (Split a String in Balanced Strings)
# @Author: cocofe
# @Date: 2020-01-26 18:02:08
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = 0 
        l_c = 0
        r_c = 0
        count = 0
        while idx < len(s):
            string = s[idx]
            if string == 'L':
                l_c += 1
            elif string == 'R':
                r_c += 1
            if l_c == r_c:
                count += 1
                l_c, r_c = 0, 0
            idx += 1
        return count
