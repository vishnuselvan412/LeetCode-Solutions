from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        phase = 0  
        # 0 = first increasing
        # 1 = decreasing
        # 2 = second increasing

        moved_up1 = moved_down = moved_up2 = False

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return False  # no flat allowed

            # 📈 Phase 0 — increasing
            if phase == 0:
                if nums[i] < nums[i + 1]:
                    moved_up1 = True
                else:  # switch to decreasing
                    if not moved_up1:
                        return False
                    phase = 1

            # 📉 Phase 1 — decreasing
            if phase == 1:
                if nums[i] > nums[i + 1]:
                    moved_down = True
                else:  # switch to second increasing
                    if not moved_down:
                        return False
                    phase = 2

            # 📈 Phase 2 — increasing again
            if phase == 2:
                if nums[i] < nums[i + 1]:
                    moved_up2 = True
                else:
                    return False  # can't go down again

        return moved_up1 and moved_down and moved_up2
