class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        if not intervals
            return -1
        
        if len(intervals) < 2:
            return intervals[0]

        sort intervals nlogn
        new result arr <- intervals[0]
        for start, end in intervals[1:]
            lastEnd = arr[-1][1]

            if  start <= lastend
                arr[-1][1] = max(lastEnd, end)
            else
                arr.append([start, end])

        return arr
        '''

        if not intervals:
            return -1

        if len(intervals) < 2:
            return [intervals[0]]

        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result