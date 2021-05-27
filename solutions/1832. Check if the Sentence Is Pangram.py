class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''s=set(sentence)
        if len(s)>=26:
            return True
        else:
            return False'''
        alphabet = set(string.ascii_lowercase)
        print(len(alphabet))
        if set(sentence.lower()) >= alphabet:
            return True
        else:
            return False
      
