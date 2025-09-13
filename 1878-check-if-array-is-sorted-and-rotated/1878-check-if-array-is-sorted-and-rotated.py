class Solution:
    def check(self, nums: List[int]) -> bool:
        #brute force method rotating array each time and checking if its sorted
        sorted_list =  sorted(nums)
        l=len(nums)
        for k in range(len(nums)):
            rotated_list = nums.copy()
            for i in range(len(nums)):
                rotated_list[(i+k)%l] =nums[i] 
            if rotated_list == sorted_list:
                return True
        return False