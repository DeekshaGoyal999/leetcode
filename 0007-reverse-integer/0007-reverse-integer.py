class Solution:
    def reverse(self, x: int) -> int:
        rev =0
        mod_val=1
        if x<0:
            mod_val = -1
        x= abs(x)
        print(x)
        while x>0:
            rem= x%10
            rev = rev*10 +rem
            x=x//10
        rev = rev*mod_val
        if rev >(2**31)-1 or rev< -2**31:
            return 0
        return rev
