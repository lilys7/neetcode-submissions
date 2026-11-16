class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], e)
            else:
                res.append([s,e])
        return res