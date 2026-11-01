class Solution:
    def isHappy(self, n: int) -> bool:
        def findRes(num):
            total = 0
            for ch in str(num):
                total += pow(int(ch), 2)
            return total
        seen = set()
        res = findRes(n)
        while res != 1:
            if res in seen:
                return False
            seen.add(res)
            res = findRes(res)
        return True
        