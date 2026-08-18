class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use two pointers, while the str still has letters left and the next letter isnt a duplicate, move the right pointer 
        lp = 0
        maxLen = 0
        chars = set()
        for rp in range(len(s)):
            while s[rp] in chars:
                chars.remove(s[lp])
                lp += 1
            chars.add(s[rp])
            maxLen = max(maxLen, rp - lp + 1)
        return maxLen


