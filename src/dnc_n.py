from util import mid_point
from dnc import dnc_kurva

def dnc_kurva_n(points, i):
    
    if len(points) == 1:
        return points, []

    titik_tengah = []
    if i == 0:
        return [points[0], points[-1]], titik_tengah

    for j in range(len(points) - 1):
        titik_tengah.append(mid_point(points[j], points[j+1], 0.5))

    kurva = []
    for j in range(len(titik_tengah) - 1):
        kiri, tengah_kiri = dnc_kurva(points[:j+2], i - 1)
        kanan, tengah_kanan = dnc_kurva(points[j+1:], i - 1)

        titik_tengah.extend(tengah_kiri)
        titik_tengah.extend(tengah_kanan)

        kurva.extend(kiri)
        kurva.extend(kanan[1:])

    return kurva, titik_tengah