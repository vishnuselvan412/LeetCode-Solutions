class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str,nums))
        n = len(nums)
        result = ""
        for i in range(n):
            for j in range(0,n - i - 1):

                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]

        result = ''.join(nums)

        if result[0] == "0":
            return "0"

        return result
                