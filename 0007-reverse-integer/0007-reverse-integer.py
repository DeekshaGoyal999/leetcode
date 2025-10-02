class Solution:
    def reverse(self, x: int) -> int:
        # #Method 1 bruute force converted each digit and concatenated it and typecasted
        # neg = False
        # if x ==0:
        #     return x
        # if x <0:
        #     neg= True
        # a= abs(x)
        # s=""
        # while(a>0):
        #     d= a%10
        #     s+=str(d)
        #     a=a//10
        # s=int(s)
        # if neg:
        #     s= -1*s
        # if s < -2**31 or s > 2**31 - 1:
        #     return 0
        # return s

    # to avoid that string conversion
        neg = False
        if x ==0:
            return x
        if x <0:
            neg= True
        a= abs(x)
        rev=0
        while(a>0):
            rev = rev * 10 + a % 10
            a //= 10
        if neg:
            rev= -1*rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev