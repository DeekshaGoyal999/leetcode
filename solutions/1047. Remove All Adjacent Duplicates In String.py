class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0                                         
        S = list(s)            
        while i < len(S) - 1:
            if S[i] == S[i + 1]:
                del S[i]
                del S[i]
                if i: i -= 1
            else: i+= 1
        return "".join(S)
     
