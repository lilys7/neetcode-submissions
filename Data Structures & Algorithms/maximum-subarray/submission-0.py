class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want to use kadanes algorithm to find max ending at i and the max total
        maxAti = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            maxAti = max(nums[i], maxAti + nums[i])
            maxTotal = max(maxTotal, maxAti)
        return maxTotal