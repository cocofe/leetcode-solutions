
// @Title: 爬楼梯 (Climbing Stairs)
// @Author: cocofe
// @Date: 2021-07-18 11:36:10
// @Runtime: 0 ms
// @Memory: 35.2 MB

class Solution {
    public int climbStairs(int n) {
        int a = 0, b = 1;
        for (int i=0; i < n; i++){
            int tmp = a;
            a = b;
            b += tmp;
        }
        return b;

    }
}
