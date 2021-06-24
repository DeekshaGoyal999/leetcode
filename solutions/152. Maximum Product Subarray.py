class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            maxpro=0
            m=max(nums)
            for i in range(len(nums)-1):
                pro=nums[i]
                for j in range(i+1,len(nums)):
                    pro*=nums[j]
                    if pro > maxpro:
                        maxpro=pro
        if m >maxpro:
            maxpro=m
        return maxpro
        
        
        
