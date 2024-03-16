from util import mid_point

def bf_kurva(points, i, t):
    result_points = [points[0], points[-1]]
    temp_result = result_points.copy()
    intermediate_points = points[1:-1]

    for j in range(i):
        temp_intermediate = []
        while (len(intermediate_points) != 0):
            temp_intermediate.append(mid_point(temp_result[0], intermediate_points[0], t))
            if (len(temp_intermediate) % 2 == 1):
                temp_result.pop(0)
            else:
                intermediate_points.pop(0)
        intermediate_points = temp_intermediate.copy()
    
        temp_result = []
        temp_result.append(result_points[0])
        for l in range(len(intermediate_points) - 1):
            temp_result.append(mid_point(intermediate_points[l], intermediate_points[l + 1], t))
        temp_result.append(result_points[-1])
        result_points = temp_result.copy()

    return result_points