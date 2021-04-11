
# @Title: 最少侧跳次数 (Minimum Sideway Jumps)
# @Author: cocofe
# @Date: 2021-04-11 14:25:22
# @Runtime: 6972 ms
# @Memory: 291.4 MB

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        dp[0][1] = 1
        dp[0][2] = 0
        dp[0][3] = 1
        for i in range(1, len(obstacles)):
            obstacle = obstacles[i]
            for no in (1,2,3):
                # no这条道路无障碍, 他的值等于上一步的值
                if obstacle != no:
                    dp[i][no] = dp[i-1][no]
            for no in (1,2,3):
                # no这条道路有障碍, 无法通过, dp[i][no] = float('inf)
                if obstacle == no:
                    continue
                # 可能存在别的道路过来最小的情况
                dp[i][no] = min([dp[i][no]] + [dp[i][_no] + 1 for _no in (1,2,3) if _no != no])
                # print(i, no, dp[i][no])
            
        return min(dp[len(obstacles)-1].values())
            
            
