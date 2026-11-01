class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #GREEDY STARTING FROM END
        point = len(nums) - 1
        #we can reach a certain point if the value at that index is >= value + index
        j = point - 1
        while point >= 0 and j >= 0:
            if nums[j] + j >= point:
                point = j
                
            else:
                if j == 0:
                    return False
            j -= 1
        return True
