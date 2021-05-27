class Solution:
    def maxDepth(self, s: str) -> int:
        '''count=[]
        for i in s:
            if i == "(":
                count.append(i)
            if i == ")":
                count.pop(i-1)
                c
        return count'''
        left_count = max_value = 0
        for item in s:
            if item == "(":
                left_count += 1
                max_value = max(left_count, max_value)
            if item == ")":
                left_count -= 1
        return max_value
            
        
                
