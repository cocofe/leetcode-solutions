
# @Title: 删除并获得点数 (Delete and Earn)
# @Author: cocofe
# @Date: 2021-05-06 01:56:07
# @Runtime: 48 ms
# @Memory: 14.9 MB

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += num
        arr = sorted(counter.keys())
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        # dp[idx][0]: 表示不取idx位置元素
        # dp[idx][1]: 表示取idx位置元素
        for idx, num in enumerate(arr):
            dp[idx][0] = max(dp[idx-1][0], dp[idx-1][1])
            if idx > 0 and arr[idx-1] == num - 1:
                # 如果上一个元素不可取, 则只有一种可能
                dp[idx][1] = dp[idx-1][0] + counter[num]
            else:
                # 如果上一个元素可取, 则取上一个元素的最大值(取或者不取)
                dp[idx][1] = dp[idx][0] + counter[num]
        return max(dp[len(arr)-1].values())






            
            

