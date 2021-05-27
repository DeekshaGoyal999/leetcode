class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        c=0
        z=0
        for i in s:
            if i=="L":
                count+=1
            if i=="R":
                c+=1
            if count == c:
                z+=1
                count=0
                c=0
        return z
                
