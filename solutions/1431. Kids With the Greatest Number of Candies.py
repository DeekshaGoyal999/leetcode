class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''n=max(candies)
        l=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=n:
                l.append(True)
            else:
                l.append(False)
        return l'''
        n=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=n:
                candies[i]=True
            else:
                candies[i]=False
        return candies
