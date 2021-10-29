        #Method-2
        m=len(matrix)
        n=len(matrix[0])
        is_col= False
        
        
        for i in range(m):
            if matrix[i][0]==0:
                is_col= True
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for k in range(1,n):
            if matrix[0][k]==0:
                for l in range(1,m):
                    matrix[l][k]=0
        for p in range(m):
            if matrix[p][0]==0:
                for y in range(1,n):
                    matrix[p][y]=0
        if matrix[0][0]==0:
            for i in range(n):
                matrix[0][i]=0
            
        if is_col:
            for i in range(m):
                matrix[i][0]=0
                
            
                    
        return matrix
                    
                    
                    
                    
                    
        
        
        
