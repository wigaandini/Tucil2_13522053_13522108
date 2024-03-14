import numpy as np
import matplotlib.pyplot as plt
import time

def kurva_bezier(p0, p1, p2, i, t):
    start_time = time.time()
    titik_kurva, titik_tengah = rec_kurva(p0, p1, p2, i, t)
    end_time = time.time()
    waktu_eksekusi = end_time - start_time
    return titik_kurva, titik_tengah, waktu_eksekusi

def kurva_bezier2(p0, p1, p2, i, t):
    start_time = time.time()
    titik_kurva = bf_kurva(p0, p1, p2, i, t)
    end_time = time.time()
    waktu_eksekusi = end_time - start_time
    return titik_kurva, waktu_eksekusi

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

def bf_kurva(p0, p1, p2, i, t):
    control_points = [p0, p1, p2]
    result_points = [p0, p2]
    intermediate_points = []

    for j in range(i):
        if (j == 0):
            for k in range(len(control_points) - 1):
                intermediate_points.append(mid_point(control_points[k], control_points[k + 1], t))
        else:
            temp_intermediate = []
            while (len(intermediate_points) != 0):
                print(f"Temp result: {temp_result}")
                print(f"Intermediate points: {intermediate_points}")
                temp_intermediate.append(mid_point(temp_result[0], intermediate_points[0], t))
                if (len(temp_intermediate) % 2 == 1):
                    temp_result.pop(0)
                else:
                    intermediate_points.pop(0)
            intermediate_points = temp_intermediate.copy()
            print(f"Intermediate points: {intermediate_points}")

        temp_result = []
        temp_result.append(result_points[0])
        for l in range(len(intermediate_points) - 1):
            temp_result.append(mid_point(intermediate_points[l], intermediate_points[l + 1], t))
        temp_result.append(result_points[-1])

        result_points = temp_result.copy()
        
        # temp_result = []
        # l = 0
        # while (len(result_points) != 0):
        #     print(f"Result points: {result_points}")
        #     if (len(temp_result) % 2 == 0):
        #         temp_result.append(result_points[0])
        #         result_points.pop(0)
        #     else: 
        #         temp_result.append(mid_point(intermediate_points[l], intermediate_points[l + 1], t))
        #         l += 1
        # result_points = temp_result.copy()

    return result_points

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

# titik_kurva, titik_tengah, waktu_eksekusi = kurva_bezier(p0, p1, p2, i, t)
titik_kurva, waktu_eksekusi = kurva_bezier2(p0, p1, p2, i, t)
print("Titik Kurva Bézier:", titik_kurva)
print("Waktu Eksekusi:", waktu_eksekusi, "detik")

show_kurva_bezier(titik_kurva, titik_kurva, p0, p1, p2)
