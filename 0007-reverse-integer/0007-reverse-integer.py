class Solution:
    def reverse(self, x: int) -> int:
        #Method 1
        # rev =0
        # mod_val=1
        # if x<0:
        #     mod_val = -1
        # x= abs(x)
        # while x>0:
        #     rem= x%10
        #     rev = rev*10 +rem
        #     x=x//10
        # rev = rev*mod_val
        # if rev >(2**31)-1 or rev< -2**31:
        #     return 0
        # return rev

        # Method-2 what if number is outside limit before chaceking
        INT_MIN= -2**31
        INT_MAX = 2**31 -1
        rev =0
        sign= -1 if x<0 else 1
        x= abs(x)
        while x>0:
            digit= x%10
            if rev > INT_MAX //10 or (rev == INT_MAX//10 and digit > (7 if sign==1 else 8)):
                return 0
            rev = rev*10 +digit
            x=x//10
        rev = rev*sign
        return rev