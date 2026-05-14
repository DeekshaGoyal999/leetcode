class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in nums:
            if i:
                nums[j]=i
                j= j+1
        nums[j:len(nums)]= [0]*(len(nums)-j)
        return nums


        