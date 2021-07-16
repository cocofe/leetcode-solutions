
# @Title: 雪糕的最大数量 (Maximum Ice Cream Bars)
# @Author: cocofe
# @Date: 2021-07-02 23:59:06
# @Runtime: 156 ms
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
