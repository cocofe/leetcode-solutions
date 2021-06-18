
// @Title: 第一个错误的版本 (First Bad Version)
// @Author: cocofe
// @Date: 2021-06-13 12:39:35
// @Runtime: 16 ms
// @Memory: 35.2 MB

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
