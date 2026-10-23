class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use the xor operation (if two bits are the same, 0, if two bits are diff, 1)
        res = 0
        for n in nums:
            res = n ^ res
        return res