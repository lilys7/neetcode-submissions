class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #a decision tree []
                    # [1]   []
                    #etc
        res = []
        def dfs(index, l):
            if index == len(nums):
                #last list appended is the final list, we have exhausted all possible combos
                res.append(l.copy())
                return

            l.append(nums[index])
            dfs(index + 1, l)
            l.pop()
            dfs(index + 1, l)
        dfs(0, [])
        return res
