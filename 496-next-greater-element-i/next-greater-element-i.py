class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            ans.append(next((x for x in nums2[index:] if x > nums2[index]),-1))
        
        return ans
        