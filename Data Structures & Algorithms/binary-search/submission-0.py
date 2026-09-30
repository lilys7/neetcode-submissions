class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            c = (rp-lp) // 2 + lp
            if nums[c] == target:
                return c
            elif nums[c] < target:
                lp = c + 1
            else:
                rp = c - 1
        return -1
