class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, l, currSum):
            if currSum > target or index == len(nums):
                return
            
            if currSum == target:
                res.append(l.copy())
                return
          
            l.append(nums[index])
            #same num
            dfs(index, l, currSum + nums[index])
            l.pop()
            dfs(index + 1, l, currSum)
        dfs(0, [], 0)
        return res



