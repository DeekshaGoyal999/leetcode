class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #Method-1
        # for i in range (0,len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if (nums[i]+nums[j]== target):
        #             return(i,j)
        #method-2 (using hashmap)
        hmap= {}
        # filling each number with it's index(count) in hmap
        for i,n in enumerate(nums):
            diff=target-n
            #if difference is found in hmap return the index stored for that differnce and n
            if diff in hmap:
                return [hmap[diff],i]
            hmap[n]=i
        return
         
    
       
            
            
            
            
       
