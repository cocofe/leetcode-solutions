
// @Title: 计数质数 (Count Primes)
// @Author: cocofe
// @Date: 2021-06-19 19:54:16
// @Runtime: 74 ms
// @Memory: 56.3 MB

class Solution {
    public int countPrimes(int n) {
        int[] primes = new int[n];
        Arrays.fill(primes, 1);
        int count = 0;
        for(int i=2; i<n; i++){
            // 默认都是素数, 从2开始遍历, 对于是素数的元素, 将素数的倍数都更新为非素数
            // 怎么保证遍历的元素没被更新过, 就一定是素数?
            // 比如15, 是3素数的倍数
            if (primes[i] == 1){
                count ++;
                for(int j=i;(long)j * i < n; j++){
                    primes[j*i] = 0;
                }
            }
        }
        return count;

    }
}
