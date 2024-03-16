from bezier import *
from input import *

while True:
    choice = input("Masukkan metode (1: brute force, 2: divide and conquer): ")
    if choice.isdigit():
        choice = int(choice)
        if choice in [1, 2]:
            break
    print("Masukkan harus berupa angka 1 atau 2. Silakan coba lagi.")

points = input_points()
i, t = input_iteration_and_t(choice)

if choice == 1:
    # bruteforce
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, False)
    print("Titik Akhir Kurva Bézier:", titik_kurva)
    print("Waktu Eksekusi:", waktu_eksekusi, "ms")
    show_kurva_bezier(points, i, t, False)
else :
    # dnc
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, True)
    print("Titik Akhir Kurva Bézier:", titik_kurva)
    print("Waktu Eksekusi:", waktu_eksekusi, "ms")
    show_kurva_bezier(points, i, t, True)