class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #    # brute force method - time O(n2), space- O(1) complexityy
    #    for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] + nums[j]== target:
    #                 return [i,j]
        
        # M-2 Dictionary
        nums_dict = {}
        for i in range(len(nums)):
            find_element = target - nums[i]
            if find_element in nums_dict:
                return [i, nums_dict[find_element]]
            else:
                nums_dict[nums[i]]=i
