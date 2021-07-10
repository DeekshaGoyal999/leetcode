class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # #Method-1
        # return 2*sum(set(nums))-sum(nums)
        
        #Method-2
        n=sorted(nums)
        print(n)
        l=0
        h=len(n)-1
        while(l<=h):
            mid=(l+h)//2
            if l==h:
                return n[l]
            elif n[mid]!=n[mid+1] and n[mid]!=n[mid-1]:
                    return n[mid]
            elif n[mid]==n[mid-1]:
                if (mid-1)%2==0:
                    l=mid+1
                else:
                    h=mid-1
            elif n[mid]==n[mid+1]:
                if (mid)%2==0:
                    l=mid+1
                else:
                    h=mid-1
                
