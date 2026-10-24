class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we want to xor the entire input list with the range list and keep track of the total output (the order doesn't matter)
        #xor the two separately?
        xororig = 0
        xorparam = 0
        for i in range(len(nums) + 1):
            xororig = xororig ^ i
        
        for n in nums:
            xorparam = xorparam ^ n
        
        return xorparam ^ xororig



