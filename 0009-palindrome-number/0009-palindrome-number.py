class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        a=x
        while(x>0):
            rev= rev*10 + x%10
            x=x//10

        # this is same as directly returing
        # if rev == a:
        #     return True
        # else:
        #     return False

        return rev == a
