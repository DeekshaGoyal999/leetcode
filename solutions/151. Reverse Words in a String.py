class Solution:
    def reverseWords(self, s: str) -> str:
        # spliting the string into list and reversing it
        # #Method-1
        # l= s.split()[::-1]
        # p=" ".join(l)
        # return p
#         # Metho-2 same thing in a line
        
#         return " ".join(s.split()[::-1])
        #Method-3 taking 2 pointers
    
        res=""
        i=len(s)-1
        while(i>=0):
            while(s[i]==" "):
                i-=1
            j=i
            while(j>=0 and s[j]!=" "):
                j-=1
            w=s[j+1:i+1]
            i=j
            print(w)
            res=res+" "+w
        return res.strip()
        
        
        
        
        
        
        
        
            
            
