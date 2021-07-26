class Solution:
    def myPow(self, x: float, n: int) -> float:
        # #Method-1
        # return pow(x,n)
        # Method -2
        if x==1:
            return x
        if n%2==0:
            sq= pow(x,n/2)
            return sq*sq
        else:
            sq= pow(x,(n-1)/2)
            return sq*sq*x
