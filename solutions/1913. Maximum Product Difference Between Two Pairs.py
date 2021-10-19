class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n=sorted(nums)
        j= (n[-1])*(n[-2])- (n[0])*(n[1])
        return j
        
