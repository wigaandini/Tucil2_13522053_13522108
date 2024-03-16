from bruteforce import bf_kurva
from dnc import dnc_kurva
import numpy as np
import matplotlib.pyplot as plt
import time

def kurva_bezier(points, i, t, dnc):
    start_time = time.time()
    if (dnc):
        titik_kurva, titik_tengah = dnc_kurva(points, i)
    else:
        titik_kurva = bf_kurva(points, i, t)
        # print("bf")
    end_time = time.time()
    waktu_eksekusi = (end_time - start_time) * 1000
    return titik_kurva, waktu_eksekusi

def show_kurva_bezier_dnc(points, iterations, dnc):
    colors = plt.cm.viridis(np.linspace(0, 1, iterations))
    for i in range(iterations):
        titik_kurva, waktu_eksekusi = kurva_bezier(points, i, 0, dnc)
        x_kurva = [titik[0] for titik in titik_kurva]
        y_kurva = [titik[1] for titik in titik_kurva]

        if i == iterations - 1:
            plt.plot(x_kurva, y_kurva, color='red', label=f"Iterasi ke-{i} ({waktu_eksekusi:.2f} ms)")
        else:
            plt.plot(x_kurva, y_kurva, color=colors[i % len(colors)], label=f"Iterasi ke-{i} ({waktu_eksekusi:.2f} ms)")

    plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label="Control Points")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Kurva Bézier')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


import matplotlib.pyplot as plt

def show_kurva_bezier_bf(titik_kurva, titik_tengah, titik_awal):
    if not isinstance(titik_kurva, list):
        titik_kurva = [titik_kurva]
    if not isinstance(titik_tengah, list):
        titik_tengah = [titik_tengah]
    if not isinstance(titik_awal, list):
        titik_awal = [titik_awal]

    x_kurva = [titik[0] for titik in titik_kurva]
    y_kurva = [titik[1] for titik in titik_kurva]

    if len(titik_tengah) > 0:
        x_tengah = [titik[0] for titik in titik_tengah]
        y_tengah = [titik[1] for titik in titik_tengah]
    else:
        x_tengah, y_tengah = [], []

    if len(titik_awal) > 0:
        x_awal = [titik[0] for titik in titik_awal]
        y_awal = [titik[1] for titik in titik_awal]
    else:
        x_awal, y_awal = [], []

    plt.plot(x_kurva, y_kurva, label="Kurva", color='blue')
    plt.scatter(x_tengah, y_tengah, color='pink', label="Titik Tengah")
    plt.scatter(x_awal, y_awal, color='red', label="Titik Awal")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Kurva Bézier')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

