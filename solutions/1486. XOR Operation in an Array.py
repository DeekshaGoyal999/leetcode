class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        s=0
        for i in range(n):
            nums.append(start + 2*i)
            s^=nums[i]
        return s
            
