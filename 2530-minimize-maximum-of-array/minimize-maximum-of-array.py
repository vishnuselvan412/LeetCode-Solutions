class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        prefixSum = 0
        answer = 0

        for i,num in enumerate(nums):
            prefixSum += num
            answer = max(answer,math.ceil(prefixSum/(i + 1)))
        return answer