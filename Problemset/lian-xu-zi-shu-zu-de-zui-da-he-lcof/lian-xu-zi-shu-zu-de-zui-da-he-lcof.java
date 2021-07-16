
// @Title: 连续子数组的最大和 (连续子数组的最大和  LCOF)
// @Author: cocofe
// @Date: 2021-07-17 00:44:55
// @Runtime: 1 ms
// @Memory: 45 MB

class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0;
        int ans = Integer.MIN_VALUE;
        for(int num : nums) {
            if (sum + num <= 0) {
                ans = Math.max(Math.max(sum+num, num), ans);
                sum = 0;
            } else {
                sum += num;
                ans = Math.max(sum, ans);
            }
        }
        return ans;

    }
}
