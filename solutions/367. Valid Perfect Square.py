class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Method-1
        # n=num**0.5
        # m= math.ceil(n)
        # print(m)
        # if m == n :
        #     return True
        # else:
        #     return False
        #Method-2
        low=1
        high=num
        
        while low<=high:
            mid=(low+high)//2
            
            if mid*mid==num:
                return True
            
            elif mid*mid>num:
                high=mid-1
                
            elif mid*mid<num:
                low=mid+1
                
        return False
            
            
