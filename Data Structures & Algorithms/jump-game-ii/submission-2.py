class Solution:
    def jump(self, nums: List[int]) -> int:
        #greedy always choose to hop to the maximum value of the available ones, or if all the same the farthest you can go.
        #always choose to hop to the one that can get u the farthest
        l = r = 0
        count = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            count += 1
        return count



