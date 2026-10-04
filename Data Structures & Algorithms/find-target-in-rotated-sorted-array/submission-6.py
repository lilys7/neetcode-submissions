class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            c = (lp + rp) // 2
            if nums[c] == target:
                return c
            if nums[lp] <= nums[c]:
                if nums[lp] <= target < nums[c]:
                    #search left side
                    rp = c - 1
                else:
                    lp = c + 1
            else:
                #right side is sorted
                if nums[c] < target <= nums[rp]:
                    lp = c+1
                else:
                    rp = c - 1
        return -1 