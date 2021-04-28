
# @Title: 滑动窗口最大值 (Sliding Window Maximum)
# @Author: cocofe
# @Date: 2021-04-29 02:06:30
# @Runtime: 448 ms
# @Memory: 27.5 MB

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        维护一个单调递减栈: 在push的时候, 如果比栈顶元素小则放入, 否则pop, 再取栈顶元素判断
        这样能保证, 最大值被移除后, 知道第二大的元素, 他就是最新的最大值
        """
        stack = collections.deque()
        ans = []
        def push(idx):
            if not stack or nums[stack[-1]] > nums[idx]:
                stack.append(idx)
            else:
                while stack and nums[stack[-1]] <= nums[idx]:
                    stack.pop()
                stack.append(idx)
        for idx in range(k):
            push(idx)
        ans.append(nums[stack[0]])
        for i in range(k, len(nums)):
            # remove
            if i - k >= stack[0]:
                stack.popleft()
            push(i)
            ans.append(nums[stack[0]])
        return ans


