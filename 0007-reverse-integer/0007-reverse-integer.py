class Solution:
    def reverse(self, x: int) -> int:
        #Method 1 bruute force converted each digit and concatenated it and typecasted it
        neg = False
        if x ==0:
            return x
        if x <0:
            neg= True
        a= abs(x)
        s=""
        while(a>0):
            d= a%10
            s+=str(d)
            a=a//10
        s=int(s)
        if neg:
            s= -1*s
        if s < -2**31 or s > 2**31 - 1:
            return 0
        return s