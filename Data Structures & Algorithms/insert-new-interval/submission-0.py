class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #sort the list first, check if the first value is less than or equal to any of the end times of other elements. Then we append the largest end time out of the two into one interval.
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        #append the first one in the result so we can get rid of an edge case
        res = [intervals[0]]
        #starts 
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
        return res
            


        