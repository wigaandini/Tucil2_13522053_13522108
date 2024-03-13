import numpy as np
import matplotlib.pyplot as plt
import time

def kurva_bezier(p0, p1, p2, i, t):
    start_time = time.time()
    titik_kurva, titik_tengah = rec_kurva(p0, p1, p2, i, t)
    end_time = time.time()
    waktu_eksekusi = end_time - start_time
    return titik_kurva, titik_tengah, waktu_eksekusi

def rec_kurva(p0, p1, p2, i, t):
    titik_tengah = []
    if i == 0:
        return [p0, p2], titik_tengah
    
    q0 = mid_point(p0, p1, t)
    q1 = mid_point(p1, p2, t)
    r0 = mid_point(q0, q1, t)
    
    kurva_kiri, tengah_kiri = rec_kurva(p0, q0, r0, i - 1, t)
    kurva_kanan, tengah_kanan = rec_kurva(r0, q1, p2, i - 1, t)
    
    titik_tengah.extend(tengah_kiri)
    titik_tengah.append(r0)
    titik_tengah.extend(tengah_kanan)
    
    return kurva_kiri + kurva_kanan[1:], titik_tengah

def mid_point(p1, p2, t):
    mid = ((1 - t) * p1[0] + t * p2[0], (1 - t) * p1[1] + t * p2[1])
    return mid

def show_kurva_bezier(titik_kurva, titik_tengah, p0, p1, p2):
    x_kurva = [titik[0] for titik in titik_kurva]
    y_kurva = [titik[1] for titik in titik_kurva]

    x_tengah = [titik[0] for titik in titik_tengah]
    y_tengah = [titik[1] for titik in titik_tengah]

    plt.plot(x_kurva, y_kurva, label="Kurva", color='blue')
    plt.scatter(x_tengah, y_tengah, color='pink', label="Titik Tengah")
    plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color='red', label="Titik Awal")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Kurva Bézier Ceunah')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Input titik kontrol
p0 = tuple(map(float, input("Koordinat p0 (pisahkan dengan spasi): ").split()))
p1 = tuple(map(float, input("Koordinat p1 (pisahkan dengan spasi): ").split()))
p2 = tuple(map(float, input("Koordinat p2 (pisahkan dengan spasi): ").split()))
i = int(input("Jumlah iterasi: "))
t = float(input("Nilai t (0 <= t <= 1): "))

titik_kurva, titik_tengah, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t)
print("Titik Kurva Bézier:", titik_kurva)
print("Waktu Eksekusi:", waktu_eksekusi, "detik")

show_kurva_bezier(titik_kurva, titik_tengah, p0, p1, p2)
