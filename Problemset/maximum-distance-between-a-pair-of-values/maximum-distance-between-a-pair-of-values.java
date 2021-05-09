
// @Title: 下标对中的最大距离 (Maximum Distance Between a Pair of Values)
// @Author: cocofe
// @Date: 2021-05-09 12:46:46
// @Runtime: 2265 ms
// @Memory: 51.3 MB

class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int p1 = 0, p2 = 0, ans = 0;
        while(p1 < nums1.length && p2 < nums2.length){
            if (nums2[p2] >= nums1[p1]) {
                ans = Math.max(p2 - p1, ans);
                p2++;
            }
            else{
                p1++;
                p2 = p1;
            }
        }
        return ans;

    }
}
