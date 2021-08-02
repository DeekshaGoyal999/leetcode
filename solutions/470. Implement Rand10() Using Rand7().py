# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
​
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while(True):
            col=rand7()
            row= (rand7()-1)*7
            if col+row<=40:
                return 1 + (col+row -1)%10
