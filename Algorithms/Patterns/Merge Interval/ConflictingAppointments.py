def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i - 1][end]:
            return False
    return True


if __name__ == '__main__':
    intervals = [[2, 4], [4, 6], [11, 12]]
    print(can_attend_all_appointments(intervals))
