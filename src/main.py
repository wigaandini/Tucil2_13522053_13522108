from bezier import *


def input_control_points():
    p0 = tuple(map(float, input("Koordinat p0 (pisahkan dengan spasi): ").split()))
    p1 = tuple(map(float, input("Koordinat p1 (pisahkan dengan spasi): ").split()))
    p2 = tuple(map(float, input("Koordinat p2 (pisahkan dengan spasi): ").split()))
    return p0, p1, p2

def input_iteration_and_t():
    i = int(input("Jumlah iterasi: "))
    t = float(input("Nilai t (0 <= t <= 1): "))
    return i, t

# Example usage:
p0, p1, p2 = input_control_points()
i, t = input_iteration_and_t()

# titik_kurva, titik_tengah, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t)

# bruteforce
titik_kurva, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t, False)
print("Titik Akhir Kurva Bézier:", titik_kurva)
print("Waktu Eksekusi:", waktu_eksekusi, "ms")
show_kurva_bezier_bf(p0, p1, p2, i, False)


# dnc
# titik_kurva, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t, True)
# print("Titik Akhir Kurva Bézier:", titik_kurva)
# print("Waktu Eksekusi:", waktu_eksekusi, "ms")
# show_kurva_bezier_dnc(p0, p1, p2, i, True)