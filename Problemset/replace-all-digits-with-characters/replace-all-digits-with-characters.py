
# @Title: 将所有数字用字符替换 (Replace All Digits with Characters)
# @Author: cocofe
# @Date: 2021-05-01 22:46:02
# @Runtime: 44 ms
# @Memory: 14.9 MB

class Solution:
    def replaceDigits(self, s: str) -> str:
        strs = []
        nums = []
        for i, _s in enumerate(s):
            if i % 2 == 0:
                strs.append(_s)
            else:
                nums.append(int(_s))
        idx = 0
        s_to_list = list(s)
        while idx * 2 + 1 < len(s_to_list):
            s_to_list[idx * 2 + 1] = chr(ord(strs[idx]) + nums[idx])
            idx += 1
        # print(s_to_list)
        return ''.join(s_to_list)
        
