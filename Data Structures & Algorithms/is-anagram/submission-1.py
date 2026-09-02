class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use ord
        if len(s) != len(t):
            return False
        charS = [0] * 26
        charT = [0] * 26
        for ch in s:
            charS[ord(ch) - ord('a')] += 1
        for ch in t:
            charT[ord(ch) - ord('a')] += 1
        if charS == charT:
            return True
        return False

        