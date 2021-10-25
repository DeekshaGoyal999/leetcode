#             return False
#         else:
#             for i in range(m):
#                 if matrix[i][0]<=target and matrix[i][-1]>=target:
#                     l=0
#                     r=len(matrix[0])
#                     while(l<=r):
#                         p=l+(r-l)//2
              
#                         if matrix[i][p]==target:
#                             return True
#                         if matrix[i][p]>target:
#                             r=p-1
#                         if matrix[i][p]<target:
#                             l=p+1
#                     if target== matrix[i][p]:
#                         return True
#         return False
        #Method-4 
        
        m= len(matrix)
        n=len(matrix[0])
        l=0
        r=(m*n)-1
       
        while(l<=r):
            mid=l+(r-l)//2      
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]>target:
                r=mid-1
            else:
                l=mid+1
        return False
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
