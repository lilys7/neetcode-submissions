class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        letters = set()
        length = 0
        for r in range(len(s)):
            while (s[r] in letters):
                letters.remove(s[lp])
                lp += 1
            letters.add(s[r])
            length = max(length, r-lp+1)
        return length
