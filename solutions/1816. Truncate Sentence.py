class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        '''l= s.split(" ")
        s=[]
        i=0
        while(k!=0):
            s.append(l[i])
            i+=1
            k-=1
        return (" ".join(s))'''
        return " ".join(s.split(" ")[0:k])
