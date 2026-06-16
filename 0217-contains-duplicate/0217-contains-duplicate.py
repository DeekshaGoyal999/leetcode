class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #M-1 set
        len_set_nums = len(set(nums))
        if len_set_nums == len(nums):
            return False
        else:
            return True
        