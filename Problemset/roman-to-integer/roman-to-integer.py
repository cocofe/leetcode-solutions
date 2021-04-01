
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: cocofe
# @Date: 2018-10-22 22:17:16
# @Runtime: 204 ms
# @Memory: N/A

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_pair = {
            "I": ("V","X"),
            "X": ("L","C"),
            "C": ("D","M")
        }
        val_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        length = len(s)

        idx = 0
        ans = 0
        while idx < length:
            if idx+1 < length and s[idx+1] in key_pair.get(s[idx], ()):
                ans += val_map[s[idx+1]] - val_map[s[idx]]
                idx += 1
            else:
                ans += val_map[s[idx]]
            idx += 1
        return ans
        
        
