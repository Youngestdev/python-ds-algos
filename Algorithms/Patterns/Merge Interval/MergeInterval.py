def mergeIntervals(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[1])
    mergedIntervals = []
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            mergedIntervals.append([start, end])
            start = interval[0]
            end = interval[1]
    mergedIntervals.append([start, end])
    return mergedIntervals

if __name__ == '__main__':
    intervals = [[1, 4], [2, 5], [7, 9]]
    print(mergeIntervals(intervals))
