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

def show_kurva_bezier(points, iterations, t, dnc):
    colors = plt.cm.viridis(np.linspace(0, 1, iterations))
    for i in range(iterations):
        titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, dnc)
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