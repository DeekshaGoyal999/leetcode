class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''c=0
        l= list(ransomNote)
        m=list(magazine)
        if set(ransomNote)<=set(magazine):
            for i in l:
                if i in m:
                    m.remove(i)
                    c+=1
            if len(ransomNote)== c:
                return True
        else:
            return False'''
        c = set(ransomNote)
        for x in c:
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True
