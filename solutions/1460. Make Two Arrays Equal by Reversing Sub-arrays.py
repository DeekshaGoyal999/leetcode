class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        '''for i in target:
            if i not in arr:
                return False
            else:
                arr.remove(i)
        else:
            return True'''
        if sorted(target) == sorted(arr):
            return True
        else:
            return False
