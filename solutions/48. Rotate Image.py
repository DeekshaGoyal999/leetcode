class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j>i:
                    temp= matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        
        for k in range(len(matrix)):
            matrix[k]=(matrix[k][::-1])
        return matrix
                    
                    
                    
        
