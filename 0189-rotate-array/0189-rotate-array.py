class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #M-1 Slicing
        k = k % len(nums)
        right_array = nums[-k:]
        left_array = nums[:-k]
        nums[:]= right_array + left_array
        return nums
        # l=len(nums)
        # for i in range(len(nums)):
        #     # a=  nums[(i+k)%l]
        #     nums[(i+k)%l] = nums[i]
        #     # nums[i] =a
        # return nums

        