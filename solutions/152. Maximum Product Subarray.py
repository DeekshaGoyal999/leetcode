class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro=max(nums)
        for i in range(len(nums)-1):
            pro=nums[i]
            for j in range(i+1,len(nums)):
                pro*=nums[j]
                if pro > maxpro:
                    maxpro=pro
        return maxpro
        
        
        
