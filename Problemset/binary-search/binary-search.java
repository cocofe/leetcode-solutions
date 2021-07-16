
// @Title: 二分查找 (Binary Search)
// @Author: cocofe
// @Date: 2021-07-17 00:49:37
// @Runtime: 0 ms
// @Memory: 39.6 MB

class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;

    }
}
