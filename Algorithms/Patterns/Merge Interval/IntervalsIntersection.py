def merge(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        a_overlaps_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]

        # check if intervals overlap and intervals_a[j]'s start time lies within the other intervals_b[i]
        b_overlaps_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        # store the the intersection part
        if a_overlaps_b or b_overlaps_a:
            result.append([max(intervals_a[i][start], intervals_b[j][start]), min(
                intervals_a[i][end], intervals_b[j][end])])

        # move next from the interval which is finishing first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


if __name__ == '__main__':
    a = [[1, 3], [5, 6], [7, 9]]
    b = [[2, 3], [5, 7]]
    c = [[1, 3], [5, 7], [9, 12]]
    d = [[5, 10]]
    print(merge(a, b))
    print(merge(c, d))
