def input_points():
    n = int(input("Number of points (minimum 2): "))
    points = []
    for i in range(n):
        if i == 0:
            points.append(tuple(map(float, input(f"Start point coordinate (separate with space): ").split())))
        elif i == n - 1:
            points.append(tuple(map(float, input(f"Final point coordinate (separate with space): ").split())))
        else:
            points.append(tuple(map(float, input(f"Coordinate of control point {i} (separate with space): ").split())))
    return points

def input_iteration_and_t(choice):
    i = int(input("Count of iteration: "))
    if choice == 1:
        t = float(input("t value (0 <= t <= 1): "))
    else :
        t = 0.5
    return i, t
