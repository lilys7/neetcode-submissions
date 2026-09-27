class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        origLength = len(intervals)
        
        #if we encounter smth that is less than the end of another, remove it from intervals and increment.
        intervals.sort(key = lambda x: x[1])
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        second = [intervals[0]]
        for s, e in intervals[1:]:
            if s < second[-1][1]:
                #remove the one with the larger end value
                #only second val matters cause we sorted, just replace the value of the second w the max
                res+=1
                second[-1][1] = min(second[-1][1], e)
            else:
                second.append([s,e])

        return res  
        



