def input_points():
    try:
        n = int(input("Number of points (minimum 2): "))
        if (n < 2):
            raise ValueError("Number of points are less than 2. ")

        points = []
        for i in range(n):
            if i == 0:
                point = tuple(map(float, input(f"Start point coordinate (separate with space): ").split()))
            elif i == n - 1:
                point = tuple(map(float, input(f"Final point coordinate (separate with space): ").split()))
            else:
                point = tuple(map(float, input(f"Coordinate of control point {i} (separate with space): ").split()))

            if len(point) != 2:
                raise ValueError("Invalid point input. ")
            points.append(point)
            
        return points
    except ValueError as ve:
        print("Invalid input: ", ve)
        raise SystemExit
    except:
        print("Something went wrong. ")
        raise SystemExit

def input_iteration_and_t(choice):
    try:
        i = int(input("Count of iteration: "))
        if (i < 0):
            raise ValueError("Invalid iteration count. ")

        if choice == 1:
            t = float(input("t value (0 <= t <= 1): "))
            if (t < 0 or t > 1):
                raise ValueError("Invalid t value. ")
        else :
            t = 0.5
        return i, t
    except ValueError as ve:
        print("Invalid input: ", ve)
        raise SystemExit
    except:
        print("Something went wrong. ")
        raise SystemExit