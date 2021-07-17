
// @Title: 丑数 (丑数 LCOF)
// @Author: cocofe
// @Date: 2021-07-18 02:42:21
// @Runtime: 48 ms
// @Memory: 38.2 MB

class Solution {
    public int nthUglyNumber(int n) {
        // 利用最小堆, 每次poll出最小的丑数, poll n次, 其中可能会offer重复的元素, 需要做去重处理
        Set<Long> visited = new HashSet<Long>();
        PriorityQueue<Long> heap = new PriorityQueue<Long>();
        visited.add(1L);
        heap.offer(1L);
        int ugly = 1;
        for (int i = 0; i < n; i++){
            long curr = heap.poll();
            ugly = (int) curr;
            long num2 = curr * 2, num3 = curr * 3, num5 = curr * 5;
            if (!visited.contains(num2)){
                heap.offer(num2);
                visited.add(num2);
            }
            if (!visited.contains(num3)){
                heap.offer(num3);
                visited.add(num3);
            }
            if (!visited.contains(num5)){
                heap.offer(num5);
                visited.add(num5);
            }
        }
        return ugly;

    }
}
