class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # taking first row for the pascal's triangle manually
        res=[[1]]
        for i in range(numRows-1):
            #creating a temporary list by appending 0 at start and end
            temp=[0]+res[-1]+[0]
            r=[]
            for j in range(len(res[-1])+1):
                # adding that temp list value 
                r.append(temp[j]+temp[j+1])
            res.append(r)
        return res
        
            
