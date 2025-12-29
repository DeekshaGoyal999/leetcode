class Solution:
    def largestOddNumber(self, num: str) -> str:
        # while(int(num)):
        #     if int(num)%2 !=0:
        #         return str(num)
        #     num=int(num)//10
        # return ""
        while(len(num)):
            if int(num[-1]) %2 !=0:
                return num
            num = num[:-1]
        return ""


