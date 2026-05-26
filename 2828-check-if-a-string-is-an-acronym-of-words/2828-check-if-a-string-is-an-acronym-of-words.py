class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word = ""
        for i in words:
            if len(i):
                word= word+i[0]
        if word == s:
            return True
        else:
            return False
        