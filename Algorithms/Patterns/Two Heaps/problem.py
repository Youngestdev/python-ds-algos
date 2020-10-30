class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  result = []
  # TODO: Write your code here
  interval = intervals[0]

  i = 0
  j = 1
  while j <= len(intervals)-1:
    if intervals[j].start >= interval.end:
      result.append(j)
      j += 1
    else:
      j += 1
    i += 1
    interval = intervals[i]

  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


if __name__ == '__main__':
    main()
