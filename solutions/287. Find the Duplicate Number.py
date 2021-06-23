import numpy as np
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Method-1
        # i=0
        # if nums[i] in nums[i+1:]:
        #     return nums[i]
        # else:
        #     return self.findDuplicate((nums[(i+1):]))
        n1=sorted(nums)
        i=0
        while(n1):
            if n1[i]==n1[i+1]:
                return n1[i]
            else:
                i=i+1
