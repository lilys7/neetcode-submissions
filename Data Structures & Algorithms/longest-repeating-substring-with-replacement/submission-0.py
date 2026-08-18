class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use ord
        l = 0
        longest = 0
        counts = [0] * 26 #for all the characters in the string
        for r in range(len(s)):
            #length of curr substring - the highest freq char > k
            counts[ord(s[r]) - ord('A')] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest