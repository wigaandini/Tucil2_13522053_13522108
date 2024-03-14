from util import mid_point

def dnc_kurva(p0, p1, p2, i):
    titik_tengah = []
    if i == 0:
        return [p0, p2], titik_tengah
    
    q0 = mid_point(p0, p1, 0.5)
    q1 = mid_point(p1, p2, 0.5)
    r0 = mid_point(q0, q1, 0.5)
    
    kurva_kiri, tengah_kiri = dnc_kurva(p0, q0, r0, i - 1)
    kurva_kanan, tengah_kanan = dnc_kurva(r0, q1, p2, i - 1)
    
    titik_tengah.extend(tengah_kiri)
    titik_tengah.append(r0)
    titik_tengah.extend(tengah_kanan)
    
    return kurva_kiri + kurva_kanan[1:], titik_tengah