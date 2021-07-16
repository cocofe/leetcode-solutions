
// @Title: 搜索插入位置 (Search Insert Position)
// @Author: cocofe
// @Date: 2021-07-17 01:04:32
// @Runtime: 0 ms
// @Memory: 38.2 MB

class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;

    }
}
