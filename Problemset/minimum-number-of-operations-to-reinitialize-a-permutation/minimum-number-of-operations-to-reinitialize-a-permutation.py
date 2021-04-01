
# @Title: 还原排列的最少操作步数 (Minimum Number of Operations to Reinitialize a Permutation)
# @Author: cocofe
# @Date: 2021-03-28 11:41:15
# @Runtime: 3276 ms
# @Memory: 13 MB

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(arr):
            perm = copy.deepcopy(arr)
            for i, a in enumerate(arr):
                if i % 2 == 0:
                    arr[i] = perm[i / 2]
                else:
                    arr[i] = perm[n / 2 + (i - 1) / 2]
            return arr
        count = 1
        perm = range(n)
        arr = helper(range(n))
        # print arr, perm
        while arr != perm:
            arr = helper(arr)
            count += 1
        return count
        
