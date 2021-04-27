
# @Title: 雪糕的最大数量 (Maximum Ice Cream Bars)
# @Author: cocofe
# @Date: 2021-04-28 01:24:56
# @Runtime: 160 ms
# @Memory: 24.8 MB

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        count = 0
        for i, cost in enumerate(costs):
            if coins >= cost:
                count += 1
                coins -= cost
            else:
                break
        return count
