class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)<1 and len(goal)<1:
            return True
        for i in range(len(s)):
            if s[i:len(s)]+s[:i] == goal:
                return True
        return False
