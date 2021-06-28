class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        k=nums[0]
        i=0
        while(k!=0):
            if i + nums[i] >= len(nums)-1:
                return True
            else:
                i=i+1
                k-=1
                if k>=nums[i]:
                    k=k
                else:
                    k=nums[i]
        return False
        
