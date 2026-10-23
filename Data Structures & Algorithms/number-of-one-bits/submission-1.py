class Solution:
    def hammingWeight(self, n: int) -> int:
        #two ways to do, we could keep doing mod 2 and doing a right shift until we get 0, in this case there will be O(32) times the while loop runs which is constant
        #Or we can do n & (n-1) which will only count the 1s and skip the 0s
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
