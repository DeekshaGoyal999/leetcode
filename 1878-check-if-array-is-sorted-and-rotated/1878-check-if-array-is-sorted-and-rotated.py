class Solution:
    def check(self, nums: List[int]) -> bool:
        #brute force method rotating array each time and checking if its sorted
        # sorted_list =  sorted(nums)
        # l=len(nums)
        # for k in range(len(nums)):
        #     rotated_list = nums.copy()
        #     for i in range(len(nums)):
        #         rotated_list[(i+k)%l] =nums[i] 
        #     if rotated_list == sorted_list:
        #         return True
        # return False
        # optimised way as this break this only happen once in the loop so to check value once its just i+1 to check in loop %n and only once it will be possible 
        rotation_error=0
        l=len(nums)
        for i in range(l):
            if nums[i]>nums[(i+1)%l]:
                rotation_error+=1
            if rotation_error>1:
                return False
        return True
        