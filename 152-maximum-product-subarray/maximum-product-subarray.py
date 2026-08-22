class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            max_out = current_max
            min_out = current_min

            current_max = max(
                num,
                num * max_out,
                num * min_out
            )

            current_min = min(
                num,
                num * max_out,
                num * min_out
            )

            result = max(result,current_max)

        return result

