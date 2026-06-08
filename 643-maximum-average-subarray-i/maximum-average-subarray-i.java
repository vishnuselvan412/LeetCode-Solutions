class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        int max = Integer.MIN_VALUE;
        int avg = 0;
        for(int i = 0 ; i < k ; i++){
            avg += nums[i];
        }
        max = avg;

        for(int i = k ; i < n ; i++){
            avg = avg + nums[i] - nums[i-k];
            max = Math.max(max, avg);
        }
        return (double) max/k;
    }
};