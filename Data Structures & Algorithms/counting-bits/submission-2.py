class Solution:
    def countBits(self, n: int) -> List[int]:
        #use the same n = n & (n-1)
        res = []
        for i in range(n + 1):
            temp = 0
            num = i
            while num:
                num &= (num - 1)
                temp += 1
            res.append(temp)
        return res