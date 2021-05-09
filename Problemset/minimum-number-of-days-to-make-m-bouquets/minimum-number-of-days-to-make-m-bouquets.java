
// @Title: 制作 m 束花所需的最少天数 (Minimum Number of Days to Make m Bouquets)
// @Author: cocofe
// @Date: 2021-05-10 03:05:23
// @Runtime: 29 ms
// @Memory: 47.7 MB

class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int left = Integer.MAX_VALUE, right = 0;
        for(int i = 0; i < bloomDay.length; i++){
            left = Math.min(left, bloomDay[i]);
            right = Math.max(right, bloomDay[i]);
        }
        int max_right = right;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if (check(bloomDay, mid, m, k)){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        System.out.println(left + " "+ max_right);
        return left > max_right ? -1 : left;

    }
    public boolean check(int[] bloomDay, int day, int m, int k){
        int flowers_cnt = 0;
        int bouquet = 0;
        for(int i = 0; i<bloomDay.length && bouquet < m;i++){
            if (bloomDay[i] <= day){
                flowers_cnt++;
                if (flowers_cnt == k){
                    flowers_cnt = 0;
                    bouquet++;
                }
            }
            else{
                flowers_cnt = 0;
            }
        }
        // System.out.println(""+day+" "+bouquet+" "+m);
        return bouquet >= m;
    }
}
