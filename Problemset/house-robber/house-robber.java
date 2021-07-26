
// @Title: 打家劫舍 (House Robber)
// @Author: cocofe
// @Date: 2021-07-24 18:37:16
// @Runtime: 0 ms
// @Memory: 35.8 MB

class Solution {
    public int rob(int[] nums) {
        int a = 0, b = 0, c = nums[0];
        for ( int i = 1; i< nums.length; i ++) {
            int tmp1 = a;
            int tmp2 = b;
            a = b;
            b = c;
            c = Math.max(tmp2, tmp1) + nums[i];
            // System.out.printf("i: %d  a:%d b:%d c:%d tmp1:%s tmp2:%s \n", i, a, b, c, tmp1, tmp2);
        }
        return Math.max(c, b);
    }
}
