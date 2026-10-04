class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        res = []

        while i < len(intervals) - 1 and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        if intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            res.append(intervals[i])
            i += 1
        elif intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            res.append(newInterval)
            i += 1
        else:
            start = min(intervals[i][0], newInterval[0])
            while i < len(intervals) - 1 and intervals[i + 1][0] <= newInterval[1]:
                i += 1
            end = max(intervals[i][1], newInterval[1])

            res.append([start, end])
            i += 1

        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res
        