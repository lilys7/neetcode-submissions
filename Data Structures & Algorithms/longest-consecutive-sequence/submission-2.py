class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert into a set for O(1) lookup
        nums = set(nums)
        start = []
        for n in nums:
            if (n-1) not in nums:
                start.append(n)
        maxLen = 0
        count = 0
        print(start)
        for i in start:
            starting = i
            count = 0
            while starting in nums:
                count+=1
                starting+=1
            maxLen = max(maxLen, count)
        return maxLen


