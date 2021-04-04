
# @Title: 绝对差值和 (Minimum Absolute Sum Difference)
# @Author: cocofe
# @Date: 2021-04-04 12:19:03
# @Runtime: 440 ms
# @Memory: 34.8 MB

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        ns1, ns2 = sorted(list(set(nums1))), sorted(list(set(nums2)))
        n1, n2 = 0, 0
        mapping = collections.defaultdict(lambda:float('inf'))
        while n1 < len(ns1) and n2 < len(ns2):
            diff = abs(ns2[n2] - ns1[n1])
            mapping[ns2[n2]] = min(mapping[ns2[n2]], diff)
            if ns2[n2] == 99:
                print mapping[ns2[n2]], n1, ns1[n1], ns2[n2], len(ns1)
            if n1 + 1 < len(ns1):
                if abs(ns2[n2] - ns1[n1+1]) >= mapping[ns2[n2]]:
                    n2 += 1
                else:
                    n1 += 1
            else:
                n2 += 1
            
        max_diff = 0
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            max_diff = max(abs(diff - mapping[n2]), max_diff)
            ans += diff
        return (ans - max_diff) % (10**9 + 7)
        
                
            
