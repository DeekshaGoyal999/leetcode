class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[]
        s=0
        l.append(0)
        for i in range(len(gain)):
            s= s+ gain[i]
            l.append(s)
        return max(l)
