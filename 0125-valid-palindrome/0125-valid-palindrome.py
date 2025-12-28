import re
class Solution:
    def isPalindrome(self, s: str,i=0) -> bool:
        s= re.sub(r'[^A-Za-z0-9]','',s)
        s=s.lower()
        # USing slicing
        if s == s[::-1]:
            return True
        return False
        

        # #using recursion
        # n=len(s)
        # if i>=n//2:
        #     return True
        # if s[i]!= s[n-i-1]:
        #     return False
        # return self.isPalindrome(s,i+1)
