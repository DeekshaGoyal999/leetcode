class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return len(nums)-1
        else:
            while l<=h:
                mid=(l+h)//2
                if nums[mid]>nums[mid+1]:
                    if nums[mid]>nums[mid-1]:
                        return mid
                    else:
                        h=mid-1
                else:
                    if nums[mid+1]>nums[mid+2]:
                        return mid+1
                    else:
                        l=mid+2
            
