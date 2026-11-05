"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        
        res = 0
        count = 0
        s = 0
        e = 0
        
        # Iterate through all start times
        while s < len(intervals):
            if start_times[s] < end_times[e]:
                # A new meeting starts before the earliest ongoing meeting ends
                count += 1
                s += 1
            else:
                # A meeting has ended, free up a room
                count -= 1
                e += 1
            
            # Track the maximum number of concurrent rooms needed
            res = max(res, count)
            
        return res