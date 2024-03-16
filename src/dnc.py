from util import mid_point

def dnc_kurva(points, i):
    titik_tengah = []
    if i == 0 or len(points) < 3:
        return [points[0], points[-1]], titik_tengah
    
    q0 = mid_point(points[0], points[1], 0.5)
    if len(points) >= 3:
        q1 = mid_point(points[1], points[2], 0.5)
        r0 = mid_point(q0, q1, 0.5)
    else:
        r0 = q0  # If there are only two points, set r0 to q0
    
    kurva_kiri, tengah_kiri = dnc_kurva([points[0], q0, r0], i - 1)
    kurva_kanan, tengah_kanan = dnc_kurva([r0, q1, points[2]], i - 1)
    
    titik_tengah.extend(tengah_kiri)
    titik_tengah.append(r0)
    titik_tengah.extend(tengah_kanan)
    
    return kurva_kiri + kurva_kanan[1:], titik_tengah
