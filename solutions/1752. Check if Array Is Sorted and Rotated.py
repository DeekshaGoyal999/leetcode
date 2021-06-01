class Solution:
    def check(self, nums: List[int]) -> bool:
        s = sorted(nums)
        z=[]
        a=len(s)
        i=0
        while(a!=0):
            z = s[i+1:] + (s[0:i+1])
            if z == nums:
                return True
            z=[]
            a-=1
            i+=1
        return False
