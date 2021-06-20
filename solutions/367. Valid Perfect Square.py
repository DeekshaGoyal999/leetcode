class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=num**0.5
        m= math.ceil(n)
        print(m)
        if m == n :
            return True
        else:
            return False
        
