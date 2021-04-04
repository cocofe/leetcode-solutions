
# @Title: 序列中不同最大公约数的数目 (Number of Different Subsequences GCDs)
# @Author: cocofe
# @Date: 2021-04-04 17:55:12
# @Runtime: 2932 ms
# @Memory: 30.3 MB

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        题意是数组元素所有的子序列下, 不同的最大公约数的个数
        - 每个元素最大公约数是自己本身
        - 某个子序列最大值不超过数组中的最大值
        """
        ans = 0
        nums = set(nums)
        max_n = max(nums)
        for i in range(1, max_n+1):
            # 判断 i 是否是某个子序列的最大公约数
            g = None
            for j in range(i, max_n+1, i):
                # 从i开始, 每次递增i, 
                # 这个序列有个特点, 就是每个元素都是 i * step (step = 1,2,3,4...)
                # 所以这个序列的最小公约数为i, gcd的结果肯定是i的倍数
                # 所以每次找到在数组中的元素的时候, 判断此子序列的最小最大公约数 = gcd(当前最大公约数, 当前元素)
                # [1,2,3,4,...] -> 最大公约数为1
                # [2,4,6,8,...] -> 最大公约数为2
                # 下面就是找是否存在子序列, 最大公约数为i
                if j not in nums:
                    # 该元素不在数组中, 忽略
                    continue
                if not g:
                    g = j
                else:
                    g = math.gcd(g, j)
                if g == i:
                    # 存在一个子序列, 使得最大公约数等于i
                    ans += 1
                    break
        return ans
