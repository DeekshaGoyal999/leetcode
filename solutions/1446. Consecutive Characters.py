class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        curr=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                curr.append(c)
                c=1
        curr.append(c)
        return max(curr)
