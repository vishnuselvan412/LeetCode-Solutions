class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        st = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0 
            st = max(st,count)
        return st