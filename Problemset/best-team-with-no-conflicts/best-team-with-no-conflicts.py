
# @Title: 无矛盾的最佳球队 (Best Team With No Conflicts)
# @Author: cocofe
# @Date: 2020-10-18 23:07:59
# @Runtime: 1840 ms
# @Memory: 13.6 MB

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        # dp[score] = dp[prev_max_score] + score
        # 队员中最大分数为score的的球队(最大)总分
        # 排序
        dp = collections.defaultdict(int)
        def find_max_scores(score):
            tracked_scores = sorted(dp.keys()) 
            ret = []
            for _s in tracked_scores:
                if _s <= score:
                    ret.append(_s)
                    continue
                break
            return ret
        mapping = collections.defaultdict(list)
        for age, score in zip(ages, scores):
            mapping[age].append(score)
        for age, scores in mapping.items():
            mapping[age] = sorted(scores)
        ans = float('-inf')
        for age in sorted(mapping.keys()):
            scores = mapping[age]
            for score in scores:
                max_scores = find_max_scores(score)
                if not max_scores:
                    _sum = score
                else:
                    _sum = max(dp[_s] for _s in max_scores) + score
                ans = max(ans, _sum)
                dp[score] = _sum
        return ans             
            
