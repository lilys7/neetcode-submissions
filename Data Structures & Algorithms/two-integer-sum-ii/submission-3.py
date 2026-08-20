class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        res = []
        for i, n in enumerate(numbers):
            nums[n] = i #num : index
        for r in range(len(numbers)):
            tar = target - numbers[r]
            if tar in nums and nums[tar] != r:
                res.append(int(r) + 1)
                res.append(int(nums[tar])+1)
                return res
        return []

            
            