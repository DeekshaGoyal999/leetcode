class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, time- O(n) , space- O(n)
        char_dict = {}
        left =0
        max_length=0
        for right in range(len(s)):
            if s[right] in char_dict:
                left = max(left, char_dict[s[right]]+1)
            char_dict[s[right]]=right
            max_length= max(max_length, right-left+1)
        return max_length


        