class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0

        for char, count in freq.items():
            if count % 2 == 0 or res % 2 == 0:
                res += count
            else:
                res += count - 1

        return res