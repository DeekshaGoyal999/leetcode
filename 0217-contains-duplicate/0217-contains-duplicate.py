class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # #M-1 set
        # len_set_nums = len(set(nums))
        # if len_set_nums == len(nums):
        #     return False
        # else:
        #     return True

        # M-2 loop O(n) - not running lime limit exceeded
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            set_nums.add(i)
        return False

        # #M-3
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False

        