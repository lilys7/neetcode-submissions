class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        mini = nums[0]
        while lp <= rp:
            c = (lp + rp) // 2
            mini = min(mini, nums[c])
            if nums[c] > nums[rp]:
                lp = c+1
            else:
                rp = c-1
        return mini

