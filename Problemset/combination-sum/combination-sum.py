
# @Title: 组合总和 (Combination Sum)
# @Author: cocofe
# @Date: 2020-11-03 23:20:38
# @Runtime: 172 ms
# @Memory: 13.5 MB

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # dp[i][j]: 取前i个元素, target为j的解集
        dp = collections.defaultdict(list)
        for i in range(len(candidates)):
            num = candidates[i]
            for j in range(1, target+1):
                if num > j:
                    continue
                if j % num == 0 and j / num > 0:
                    dp[j].append([num] * (j / num))
                tmp = copy.deepcopy(dp[j-num])
                for _tmp in tmp:
                    _tmp.append(num)
                    if _tmp not in dp[j]:
                        dp[j].append(_tmp)
        return dp[target]
