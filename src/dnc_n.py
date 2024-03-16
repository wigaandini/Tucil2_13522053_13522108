from util import mid_point
from dnc import dnc_kurva  # Assuming this function is correctly implemented

def dnc_kurva_n(points, i):
    if len(points) == 1:
        return points, []

    titik_tengah = []
    if i == 0:
        return [points[0], points[-1]], titik_tengah

    # Calculate intermediate points
    for j in range(len(points) - 1):
        titik_tengah.append(mid_point(points[j], points[j+1], 0.5))

    kurva = []
    for j in range(len(titik_tengah) - 1):
        # Divide the curve into left and right segments
        kiri, tengah_kiri = dnc_kurva(points[:j+2], i - 1)
        kanan, tengah_kanan = dnc_kurva(points[j+1:], i - 1)

        # Combine the left and right segments
        kurva.extend(kiri)
        kurva.extend(kanan[1:])  # Skip the duplicate point between left and right segments

        # Extend the list of intermediate points
        titik_tengah.extend(tengah_kiri)
        titik_tengah.extend(tengah_kanan)

    return kurva, titik_tengah
