class Solution:
    def countneg(self, lst: List[int]) -> int:
        count=0
        n=len(lst)
        l=0
        r=n-1
        while(l<=r):
            mid= (l+r)//2
            if lst[mid]>=0:
                l=mid+1
            elif lst[mid]<0:     
                count+=r-mid+1
                r=mid-1
        return count
        
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for item in grid:
            count += self.countneg(item)
        return count
