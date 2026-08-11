class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap with value and index. if the sub val exists, return indeces
        values = {}
        ret = []
        for i, num in enumerate(nums):
            values[num] = i
        
        for num in nums:
            sub = target - num
            if sub in values and nums.index(num) != values[sub]:
                ret.append(nums.index(num))
                ret.append(values[sub])
                return ret
        return ret