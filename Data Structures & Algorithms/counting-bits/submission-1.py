class Solution:
    def countBits(self, n: int) -> List[int]:
        #same as before n & (n-1) but now for every num in the range of n
        res = []
        for num in range(0,n + 1):
            temp = 0
            i = num
            while i:
                i = i & (i-1)
                temp += 1
            res.append(temp)
        return res