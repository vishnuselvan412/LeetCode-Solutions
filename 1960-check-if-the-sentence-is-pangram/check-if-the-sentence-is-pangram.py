class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        st = 'abcdefghijklmnopqrstuvwxyz'

        return len(set(sentence)) == 26