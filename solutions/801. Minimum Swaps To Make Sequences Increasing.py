class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        n=len(nums1)
        swap=[0]*n
        noswap=[0]*n
        swap[0]=1
        noswap[0]=0
        
        for i in range(1,len(nums1)):
            inc = nums1[i-1]< nums1[i] and nums2[i-1]< nums2[i]
            xinc= nums1[i-1]<nums2[i] and nums2[i-1]< nums1[i]
            if inc and xinc:
                swap[i]= min(swap[i-1],noswap[i-1])+1
                noswap[i]=min(swap[i-1],noswap[i-1])
            elif inc:
                swap[i]=swap[i-1]+1
                noswap[i] =noswap[i-1]
            elif xinc:
                swap[i]= 1 + noswap[i-1]
                noswap[i]=swap[i-1]
        return min(swap[n-1],noswap[n-1])
​
