
# @Title: 森林中的兔子 (Rabbits in Forest)
# @Author: cocofe
# @Date: 2021-04-04 18:10:29
# @Runtime: 48 ms
# @Memory: 15 MB

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # 5 出现 8次: 6只兔子颜色一样, 如果只有一种颜色, 则可以出现最多6次, 如果有两种颜色, 则最多出现 6*2次
        counter = collections.Counter(answers)
        ans = 0
        for num, cnt in counter.items():
            ans += (num + 1) * (cnt // (num + 1))
            if cnt % (num + 1) != 0:
                ans += num + 1
        return ans
