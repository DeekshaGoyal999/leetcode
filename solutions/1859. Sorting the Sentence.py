class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split(" ")
        p=[""]*len(l)
        for i in range(len(l)):
            p[int(l[i][-1])-1] = l[i][:-1]
        return (" ".join(p))
