import re
class Solution:
    def isPalindrome(self, s: str,i=0) -> bool:
        # #M-1
        # s= re.sub(r'[^A-Za-z0-9]','',s) # time - O(n) space- O(n) new string cretaed
        # s=s.lower() #time - O(n) space- O(n) 
        # # USing slicing
        # if s == s[::-1]: #time - O(n) space- O(n) 
        #     return True
        # return False
        

        # #using recursion
        # n=len(s)
        # if i>=n//2:
        #     return True
        # if s[i]!= s[n-i-1]:
        #     return False
        # return self.isPalindrome(s,i+1)

        #m-3 two pointer
        left =0
        right = len(s)-1
        while right>left:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower() !=s[right].lower():
                return False
            left +=1
            right-=1
        return True
    
            
            
            
