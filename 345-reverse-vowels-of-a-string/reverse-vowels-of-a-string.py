class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        st = ""
        re = ""
       
        vl = [c for c in s if c in vowels]

        rev = vl[::-1]

        j=0
        ans=""

        for c in s:
            if c in vowels:
                ans += rev[j]
                j+=1
            else:
                ans += c
        return ans