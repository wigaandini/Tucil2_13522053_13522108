from bezier import *

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

def input_iteration_and_t(choice):
    i = int(input("Jumlah iterasi: "))
    if choice == 1:
        t = float(input("Nilai t (0 <= t <= 1): "))
    else :
        t = 0.5
    return i, t

# Example usage:
while True:
    choice = input("Masukkan metode (1: brute force, 2: divide and conquer): ")
    if choice.isdigit():
        choice = int(choice)
        if choice in [1, 2]:
            break
    print("Masukkan harus berupa angka 1 atau 2. Silakan coba lagi.")
points = input_points()
i, t = input_iteration_and_t(choice)

# titik_kurva, titik_tengah, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t)


if choice == 1:
    # bruteforce
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, False)
    print("Titik Akhir Kurva Bézier:", titik_kurva)
    print("Waktu Eksekusi:", waktu_eksekusi, "ms")
    show_kurva_bezier(points, i, t, False)
else :
    # dnc
    print(points)
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, True)
    print("Titik Akhir Kurva Bézier:", titik_kurva)
    print(len(titik_kurva))
    print("Waktu Eksekusi:", waktu_eksekusi, "ms")
    show_kurva_bezier(points, i, t, True)