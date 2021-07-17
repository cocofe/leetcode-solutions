
// @Title: 机器人的运动范围 (机器人的运动范围  LCOF)
// @Author: cocofe
// @Date: 2021-07-17 02:01:18
// @Runtime: 2 ms
// @Memory: 37.7 MB

class Solution {

    private int count = 0;

    public int movingCount(int m, int n, int k) {
        boolean[][] visited = new boolean[m][n];
        backtrace(0, 0, visited, m-1, n-1, k);
        return count;
    }
    
    private void backtrace(int x, int y, boolean[][] visited, int xEnd, int yEnd, int k) {
        String toStr = String.valueOf(x) + String.valueOf(y);
        if (x > xEnd || y > yEnd || visited[x][y] || (x % 10 + x / 10 + y % 10 + y / 10) > k) {
            return;
        }
        count ++;
        visited[x][y] = true;
        backtrace(x + 1, y, visited, xEnd, yEnd, k);
        backtrace(x, y+1, visited, xEnd, yEnd, k);
    }
}
