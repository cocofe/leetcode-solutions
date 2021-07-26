
// @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
// @Author: cocofe
// @Date: 2021-07-24 18:09:37
// @Runtime: 1 ms
// @Memory: 38.1 MB

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int a = cost[0], b = cost[1];
        for (int i=2; i< cost.length; i ++) {
            int tmp = a;
            a = b;
            b = Math.min(tmp, b) + cost[i];
        }
        return Math.min(a, b);
        

    }
}
