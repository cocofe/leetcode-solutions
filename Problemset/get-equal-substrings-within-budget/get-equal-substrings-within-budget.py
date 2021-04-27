
# @Title: 尽可能使字符串相等 (Get Equal Substrings Within Budget)
# @Author: cocofe
# @Date: 2021-04-27 02:23:11
# @Runtime: 344 ms
# @Memory: 19.9 MB

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def helper(left, right, i):
            # 找到最左侧边界
            while left <= right:
                mid = left + (right - left) // 2
                if _adds[i] - _adds[mid] <= maxCost:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        nums = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]
        _sum = 0
        _adds = []
        for num in nums:
            _sum += num
            _adds.append(_sum)
        ans = 0
        for i in range(len(s)):
            if _adds[i] <= maxCost:
                ans = max(ans, i + 1)
                continue
            j = helper(0, i, i)
            ans = max(ans, i - j)
        return ans

