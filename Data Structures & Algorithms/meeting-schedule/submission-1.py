"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last = None
        intervals.sort(key = lambda x:x.start)
        for obj in intervals:
            s = obj.start
            e = obj.end
            if last is None:
                last = e
            elif s < last:
                return False
            else:
                last = e
        return True