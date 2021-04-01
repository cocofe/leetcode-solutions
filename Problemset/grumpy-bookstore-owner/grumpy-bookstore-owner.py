
# @Title: 爱生气的书店老板 (Grumpy Bookstore Owner)
# @Author: cocofe
# @Date: 2021-02-24 02:06:33
# @Runtime: 252 ms
# @Memory: 16.4 MB

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        left, right = 0, 0
        total_sum = sum([cum for cum, grm in zip(customers, grumpy) if grm == 0])
        increase = sum([grumpy[i] * customers[i] for i in range(X)])
        max_inc = increase
        for i in range(X, len(customers)):
            increase = increase - grumpy[i-X] * customers[i-X] + grumpy[i] * customers[i]
            max_inc = max(max_inc, increase)
        return max_inc + total_sum
            
            
            
                    


            
