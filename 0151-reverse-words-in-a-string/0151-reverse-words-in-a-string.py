class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        rev_l = l[::-1]
        new_s=" ".join(rev_l)
        return new_s
        