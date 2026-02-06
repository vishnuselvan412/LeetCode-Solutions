class Solution {
    public int minMoves2(int[] nums) {
        int sum = 0;
        Arrays.sort(nums);
        int mid = nums.length/2;
        if (nums.length == 1 || nums.length == 0) return 0;
        for(int i=0;i<nums.length;i++){
            sum+=Math.abs(nums[i]-nums[mid]);
        }
        return sum;
    }
}