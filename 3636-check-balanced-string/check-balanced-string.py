class Solution:
    def isBalanced(self, num: str) -> bool:
        s = 0
        neg = 0
        for i in range(len(num)):
            if i % 2 == 0:
                s=s+int(num[i])
            else:
                neg=neg+int(num[i])
        return s==neg