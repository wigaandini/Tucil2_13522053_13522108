from bruteforce import bf_kurva
from dnc import dnc_kurva
from dnc_n import dnc_kurva_n
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

def kurva_bezier(points, i, t, dnc):
    start_time = time.time()
    if (dnc):
        titik_kurva, titik_tengah = dnc_kurva_n(points, i)
    else:
        titik_kurva = bf_kurva(points, i, t)
    end_time = time.time()
    waktu_eksekusi = (end_time - start_time) * 1000
    return titik_kurva, waktu_eksekusi


# with animation
def show_kurva_bezier(points, iterations, t, dnc):
    def update(frame):
        plt.cla()
        colors = plt.cm.viridis(np.linspace(0, 1, frame + 1))
        for i in range(frame + 1):
            titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, dnc)
            x_kurva = [titik[0] for titik in titik_kurva]
            y_kurva = [titik[1] for titik in titik_kurva]

            if i == frame:
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

    fig = plt.figure()
    update(iterations)
    ani = FuncAnimation(fig, update, frames=iterations + 1, interval=1000, repeat=False)
    plt.show()


# without animation
# def show_kurva_bezier(points, iterations, t, dnc):
#     colors = plt.cm.viridis(np.linspace(0, 1, iterations))
#     for i in range(iterations+1):
#         titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, dnc)
#         x_kurva = [titik[0] for titik in titik_kurva]
#         y_kurva = [titik[1] for titik in titik_kurva]

#         if i == iterations:
#             plt.plot(x_kurva, y_kurva, color='red', label=f"Iterasi ke-{i} ({waktu_eksekusi:.2f} ms)")
#         else:
#             plt.plot(x_kurva, y_kurva, color=colors[i % len(colors)], label=f"Iterasi ke-{i} ({waktu_eksekusi:.2f} ms)")

#     plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label="Control Points")
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Kurva Bézier')
#     plt.legend()
#     plt.grid(True)
#     plt.axis('equal')
#     plt.show()