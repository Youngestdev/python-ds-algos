def insertIntervals(intervals, newInterval):
        merged = []
        i, start, end = 0, 0, 1

        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        merged.append(newInterval)

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

if __name__ == '__main__':
    intervals = [[1, 3], [5, 7], [8, 12]]
    new_interval = [4, 6]
    print(insertIntervals(intervals, new_interval))