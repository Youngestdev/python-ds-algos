def array_advance(a):
    furthest_reached = 0
    last_index = len(a) - 1
    i = 0

    while i <= furthest_reached <= last_index:
        furthest_reached = max(furthest_reached, a[i] + i)
        i += 1
    return furthest_reached >= last_index
