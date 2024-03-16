from util import mid_point

def bf_kurva(control_points, i, t):
    result_points = [control_points[0], control_points[-1]]
    intermediate_points = []

    for j in range(i):
        if j == 0:
            for k in range(len(control_points) - 1):
                intermediate_points.append(mid_point(control_points[k], control_points[k + 1], t))
        else:
            temp_intermediate = []
            while len(intermediate_points) != 0:
                temp_intermediate.append(mid_point(temp_result[0], intermediate_points[0], t))
                if len(temp_intermediate) % 2 == 1:
                    temp_result.pop(0)
                else:
                    intermediate_points.pop(0)
            intermediate_points = temp_intermediate.copy()

        temp_result = [result_points[0]]
        for l in range(len(intermediate_points) - 1):
            temp_result.append(mid_point(intermediate_points[l], intermediate_points[l + 1], t))
        temp_result.append(result_points[-1])
        result_points = temp_result.copy()

    return result_points
