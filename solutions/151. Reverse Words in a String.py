class Solution:
    def reverseWords(self, s: str) -> str:
        # spliting the string into list and reversing it
        # #Method-1
        # l= s.split()[::-1]
        # p=" ".join(l)
        # return p
        # Metho-2 same thing in a line
        
        return " ".join(s.split()[::-1])
        
            
            
