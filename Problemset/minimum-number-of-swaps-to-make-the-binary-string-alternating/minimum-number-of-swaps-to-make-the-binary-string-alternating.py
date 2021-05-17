
# @Title: 构成交替字符串需要的最小交换次数 (Minimum Number of Swaps to Make the Binary String Alternating)
# @Author: cocofe
# @Date: 2021-05-16 11:04:49
# @Runtime: 72 ms
# @Memory: 16.1 MB

class Solution:
    def minSwaps(self, s: str) -> int:
        # counter[1] = 2 表示1变成0的次数
        # 替换0变成1 -> counter[0] ++
        counter = [0, 0]
        def helper(idx, expect_char, count):
            if idx >= len(s):
                if counter[0] == counter[1]:
                    return count // 2
                return None
            next_char = '1' if expect_char == '0' else '0'
            if s[idx] == expect_char:
                return helper(idx+1, next_char, count)
            counter[int(s[idx])] += 1
            return helper(idx+1, next_char, count+1)
        ret = -1
        for char in ['0', '1']:
            ans = helper(0, char, 0)
            counter = [0, 0]
            if ans is not None:
                if ret == -1:
                    ret = ans
                else:
                    ret = min(ret, ans)
        return ret
        
