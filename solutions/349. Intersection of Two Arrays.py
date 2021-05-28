class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #method 1
        m=set(nums1)
        n=set(nums2)
        l=[]
        for i in m:
            if i in n:
                l.append(i)
        return l
        #method 2
        '''m=set(nums1)
        n=set(nums2)
        
        return(list(m.intersection(n)))'''
