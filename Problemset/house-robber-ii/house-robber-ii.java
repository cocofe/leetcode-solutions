
// @Title: 打家劫舍 II (House Robber II)
// @Author: cocofe
// @Date: 2021-07-24 18:52:42
// @Runtime: 0 ms
// @Memory: 36 MB

class Solution {
    public int rob(int[] nums) {
        return Math.max(helper(nums, 0, nums.length-2), helper(nums, 1, nums.length-1));
    }
    private int helper(int[] nums, int i, int j){
        if (i >= nums.length) {
            return 0;
        }
        int a=0, b = 0, c = nums[i];
        for (int idx=i+1; idx <= j; idx ++) {
            int tmp1 = a, tmp2 = b;
            a = b;
            b = c;
            c = Math.max(tmp1, tmp2) + nums[idx];
            // System.out.printf("idx:%s, a:%s, b:%s, c:%s \n", idx, a, b, c);
        }
        // System.out.printf("i:%s j:%s -> %s\n", i, j, Math.max(b, c));
        return Math.max(b, c);
    }
}
