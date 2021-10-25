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
        #Method-2
        for i in range(len(matrix)):
                if matrix[i][0]<=target and matrix[i][-1]>=target:
                    if target in matrix[i]:
                        return True
        return False
                    
                    
                    
                    
                    
                    
                    
        
