class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        output=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            output.append(count)
        return output
        