def mid_point(p1, p2, t):
    mid = ((1 - t) * p1[0] + t * p2[0], (1 - t) * p1[1] + t * p2[1])
    return mid