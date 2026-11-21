class Solution:
    def isPalindrome(self, x: int) -> bool:
        #M-1
        # rev=0
        # a=x
        # if x<0:
        #     return False
        # while(x>0):
        #     rev= rev*10 + x%10
        #     x=x//10

        # # this is same as directly returing
        # # if rev == a:
        # #     return True
        # # else:
        # #     return False

        # return rev == a

        #M-2 this can be done in half interation rather than looping through entire integer

        # negative cant be palindrome or number ending with 0 cant be
        if x<0 or (x %10 ==0 and x!=0):
            return False
        rev=0
        while x > rev:
            rev = rev*10 + x%10
            x=x//10
        
        # if x= even thn need to check if interation is equal if odd then remove last digt from rev and compare
        return x == rev or x == rev//10