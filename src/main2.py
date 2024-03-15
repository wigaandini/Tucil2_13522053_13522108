from bezier2 import *

def input_points():
    n = int(input("Jumlah titik: "))
    points = []
    for i in range(n):
        if i == 0:
            points.append(tuple(map(float, input(f"Koordinat titik awal (pisahkan dengan spasi): ").split())))
        elif i == n - 1:
            points.append(tuple(map(float, input(f"Koordinat titik akhir (pisahkan dengan spasi): ").split())))
        else:
            points.append(tuple(map(float, input(f"Koordinat titik kontrol {i} (pisahkan dengan spasi): ").split())))
    return points


def input_iteration_and_t():
    i = int(input("Jumlah iterasi: "))
    t = float(input("Nilai t (0 <= t <= 1): "))
    return i, t



points = input_points()
i, t = input_iteration_and_t()

kurva, titik_tengah = dnc_kurva_n(points, i)
show_kurva_bezier_dnc(points, i)