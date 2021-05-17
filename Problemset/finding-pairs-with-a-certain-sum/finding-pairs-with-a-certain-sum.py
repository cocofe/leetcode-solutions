
# @Title: 找出和为指定值的下标对 (Finding Pairs With a Certain Sum)
# @Author: cocofe
# @Date: 2021-05-16 11:35:28
# @Runtime: 380 ms
# @Memory: 43.4 MB

import threading
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter2 = collections.Counter(nums2)
        self.counter1 = collections.Counter(nums1)
        self.nums2 = nums2
        self.lock = threading.Lock()


    def add(self, index: int, val: int) -> None:
        orig_val = self.nums2[index]
        self.counter2[orig_val] -= 1
        self.counter2[orig_val+val] += 1
        self.nums2[index] = orig_val+val


    def count(self, tot: int) -> int:
        ans = 0
        for num, cnt in self.counter1.items():
            if num >= tot:
                continue
            cnt2 = self.counter2.get(tot-num, 0)
            ans += cnt2 * cnt
            # print('find num %s cnt %s, tot-num %s cnt2 %s' % (num, cnt, tot-num, cnt2))
        return ans



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
