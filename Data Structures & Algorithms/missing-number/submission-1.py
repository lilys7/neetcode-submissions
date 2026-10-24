class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we want to xor the entire input list with the range list and keep track of the total output (the order doesn't matter)
        #xor the two separately?
        xorparam = 0
        
        for i, n in enumerate(nums):
            xorparam = xorparam ^ n ^ i
            if i == len(nums) - 1:
                xorparam = xorparam ^ (i+1)
        
        return xorparam



