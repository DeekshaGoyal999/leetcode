class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)>len(word2):
            l=len(word2)
            k=word1[l:]
        else:
            l=len(word1)
            k=word2[l:]
        a=""
        for i in range(l):
            a+=word1[i]
            a+=word2[i]
        
        a+=k
        return a
        
        
        
