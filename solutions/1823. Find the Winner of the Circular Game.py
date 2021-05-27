class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        while(len(l)>1):
            for j in range(0,k-1):
                m=l[0]
                l.remove(m)
                l.append(m)
            l.remove(l[0])
        return l[0]
            
            
            
        """l=[]
            for i in range(1,n+1):
                l.append(i) 
            while(len(l)!=1):   
                if k>len(l):
                    k=len(l)-k
                else:
                    k=k
                l.remove(l[k-1])
                k= k+k-1
            return l
            #print(len(l))
            #while(k!=0):
                #l.remove(l[k-1])
                
            '''for p in range(len(l)-1):
                if p>n:
                    p=p-n
                else:
                    p=p 
                while(k!=0): 
                    l.remove(l[p+k-1])
                print(l[p+k-1])'''"""
            
                        
                    
