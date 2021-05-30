class Solution:
    def firstUniqChar(self, s: str) -> int:
        r=sorted((collections.Counter(s).items()), key=lambda x:x[1], reverse=False)[0]
        if r[1] ==1:
            return s.index(r[0])
        else:
            return -1
