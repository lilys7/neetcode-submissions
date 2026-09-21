class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mapped and mapped[complement] != i:
                return [mapped[complement], i]
            else:
                mapped[num] = i
        return []
