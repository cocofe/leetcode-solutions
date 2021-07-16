
// @Title: 主要元素 (Find Majority Element LCCI)
// @Author: cocofe
// @Date: 2021-07-10 03:10:42
// @Runtime: 1 ms
// @Memory: 44.5 MB

class Solution {
    public int majorityElement(int[] nums) {
        int aliveCount = 0;
        int alive = -1;
        for (int num : nums) {
            if (aliveCount == 0) {
                alive = num;
                aliveCount ++;
                continue;
            }
            if (alive == num) {
                aliveCount++;
            } else {
                aliveCount --;
            }
        }
        if (aliveCount == 0) {
            return -1;
        }
        int count = 0;
        for (int num : nums) {
            if (num == alive) {
                count ++;
            }
        }
        return count > nums.length / 2 ? alive : -1;

    }
}
