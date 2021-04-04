
# @Title: 每日温度 (Daily Temperatures)
# @Author: cocofe
# @Date: 2021-04-04 18:29:54
# @Runtime: 548 ms
# @Memory: 19.6 MB

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = []
        for idx, t in enumerate(T[::-1]):
            while stack:
                if stack[-1][1] <= t:
                    stack.pop()
                else:
                    break
            ans.append(idx - stack[-1][0] if stack else 0)
            stack.append((idx,t))
        return ans[::-1]
