class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #use ord and chars, sliding window of fixed size len(s1)
        if len(s1) > len(s2):
            return False
        window = len(s1)
        l = 0
        chars = [0] * 26
        for r in range(len(s1)):
            chars[ord(s1[r]) - ord('a')] += 1
        while l + window <= len(s2):
            chars2 = [0] * 26

            for m in range(l, l+ window):
                chars2[ord(s2[m]) - ord('a')] += 1
            if chars == chars2:
                return True
            else:
                l += 1
        return False

