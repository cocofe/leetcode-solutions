
// @Title: 完成所有工作的最短时间 (Find Minimum Time to Finish All Jobs)
// @Author: cocofe
// @Date: 2021-05-08 01:57:52
// @Runtime: 2 ms
// @Memory: 35.7 MB

class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        Arrays.sort(jobs);
        int left = jobs[0], right = Arrays.stream(jobs).sum();
        while(left <= right){
            int mid = left + (right - left) / 2;
            int[] works = new int[k];
            if(isFinish(mid, works, jobs.length - 1, jobs)){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }
    public boolean isFinish(int limit, int[] works, int job_idx, int[] jobs){
            if(job_idx < 0){
                return true;
            }
            for(int idx=0; idx < works.length; idx++){
                if (works[idx] + jobs[job_idx] <= limit){
                    works[idx] += jobs[job_idx];
                    if(isFinish(limit, works, job_idx-1, jobs)){
                        return true;
                    }
                    works[idx] -= jobs[job_idx];
                }
                if(works[idx] == 0 || (works[idx] + jobs[job_idx] == limit)){
                    break;
                }
            }
            return false;
        }
}
