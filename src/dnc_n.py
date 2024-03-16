from util import mid_point

# Berlaku untuk n titik
def dnc_kurva_n(points, i):
    titik_tengah = []
    if i == 0:
        return [points[0], points[-1]], titik_tengah
    

    intermediate_points = points.copy()
    left_points = [points[0]]
    right_points = [points[-1]]
    temp = []
    for j in range(1, len(points)):
        for k in range(len(intermediate_points) - 1):
            temp.append(mid_point(intermediate_points[k], intermediate_points[k + 1], 0.5))
        intermediate_points = temp.copy()
        left_points.append(intermediate_points[0])
        right_points.insert(0, intermediate_points[-1])
        temp = []

    kurva_kiri, tengah_kiri = dnc_kurva_n(left_points, i - 1)
    kurva_kanan, tengah_kanan = dnc_kurva_n(right_points, i - 1)
    
    titik_tengah.extend(tengah_kiri)
    titik_tengah.extend(intermediate_points)
    titik_tengah.extend(tengah_kanan)
    
    return kurva_kiri + kurva_kanan[1:], titik_tengah