class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # #Method-1
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==target:
        #             return True
        #         else:
        #             pass
        # return False
        # #Method-2
        # for i in range(len(matrix)):
        #         if matrix[i][0]<=target and matrix[i][-1]>=target:
        #             if target in matrix[i]:
        #                 return True
        # return False
        #Method-3
        m=len(matrix)
        n=len(matrix[0])
        if target<matrix[0][0] or target> matrix[-1][-1]:
            return False
        else:
            for i in range(m):
                if matrix[i][0]<=target and matrix[i][-1]>=target:
                    l=0
                    r=len(matrix[0])
                    while(l<=r):
                        p=l+(r-l)//2
              
                        if matrix[i][p]==target:
                            return True
                        if matrix[i][p]>target:
                            r=p-1
                        if matrix[i][p]<target:
                            l=p+1
                    if target== matrix[i][p]:
                        return True
        return False
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
