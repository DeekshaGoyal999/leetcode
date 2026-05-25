class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # M-1 sorting overall time= O(nlogn), spcae =O(n) (used in creating that list)
        # if len(s)!= len(t): # time= O(1)
        #     return False
        # if sorted(s) == sorted(t): #time for sorting = O(nlogn) and for array comparison= O(n)
        #     return True
        # else:
        #     return False

        #M-2 Hasmap time= O(n), space = O(n) - new hasmap created
        
        if len(s) != len(t):
            return False
        count = {}

        for char in s: #time= O(n)
            count[char] = count.get(char,0)+1
        
        for char in t: #time= O(n)
            if char not in count:
                return False
            count[char] -=1
            if count[char]<0:
                return False
        return True
