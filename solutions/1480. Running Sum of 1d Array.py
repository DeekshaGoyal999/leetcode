class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''runningsum=0
        l=[]
        for i in range(len(nums)):
            runningsum=runningsum+nums[i]
            l.append(runningsum)
        return l'''
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
