class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # Method 1
        '''res=[]
        for i in range(0,len(nums),2):
            while(nums[i]!=0):
                m=nums[i+1]
                res.append(m)
                nums[i]=nums[i]-1
        return res'''
        # Method 2
        '''res= []
        for i in range(0,len(nums),2):
            new_list=[]
            new_list.extend(repeat(nums[i+1],nums[i]))
            #result=int(nums[i]*str(nums[i+1]))
            res= res+new_list
        return res'''
        new_list=[]
        for i in range(0,len(nums),2): 
            new_list.extend([nums[i+1]]*nums[i])
        return new_list
       
