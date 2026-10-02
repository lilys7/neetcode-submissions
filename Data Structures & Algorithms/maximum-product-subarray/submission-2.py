class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #same as kadane's algorithm but instead of addition do multiplication?
        #need to account for negative multiplication
        maxAti = nums[0]
        minAti = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            tempMax = maxAti
            maxAti = max(nums[i], nums[i] * minAti, nums[i] * maxAti)
            minAti = min(nums[i], nums[i] * minAti, nums[i] * tempMax)
            
            maxTotal = max(maxTotal, maxAti)
        return maxTotal