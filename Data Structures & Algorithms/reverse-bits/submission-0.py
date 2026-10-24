class Solution:
    def reverseBits(self, n: int) -> int:
        #we can do a mod and append the value to the beginning and sdo right shift afrer
        res = 0
        for i in range(32):
            res = res << 1
            temp = n % 2
            res += temp
            n = n >> 1
        return res
