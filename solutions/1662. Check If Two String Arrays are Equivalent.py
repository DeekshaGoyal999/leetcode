class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i="".join(word1)
        j="".join(word2)
        if i == j:
            return True
        else:
            return False
