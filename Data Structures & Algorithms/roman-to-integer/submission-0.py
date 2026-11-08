class Solution:
    def romanToInt(self, s: str) -> int:
        #if the next one is larger in value than the current one, add negative current value?
        mapped = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        p = 0
        totalNum = 0
        while p + 1 < len(s) or p == len(s) - 1:
            if p == len(s) - 1:
                totalNum += mapped[s[p]]
                break
            if mapped[s[p]] < mapped[s[p + 1]]:
                totalNum -= mapped[s[p]]
            else:
                totalNum += mapped[s[p]]
            p += 1
        return totalNum


