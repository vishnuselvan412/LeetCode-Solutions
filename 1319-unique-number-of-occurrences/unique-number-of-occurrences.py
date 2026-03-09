class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for n in arr:
            count[n] = count.get(n,0)+1

        occurences = list(count.values())
        return len(occurences) == len(set(occurences))