class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        prod=1
        while(n!=0):
            rem=n%10
            sum1+=rem
            prod*=rem
            n//=10
        return (prod-sum1)
