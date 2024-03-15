from dnc_n import dnc_kurva_n
import numpy as np
import matplotlib.pyplot as plt

def show_kurva_bezier_dnc(points, iterations):
    colors = plt.cm.viridis(np.linspace(0, 1, iterations))
    
    for i in range(iterations):
        bezier_curve, _ = dnc_kurva_n(points, i)
        x_kurva = [point[0] for point in bezier_curve]
        y_kurva = [point[1] for point in bezier_curve]
        plt.plot(x_kurva, y_kurva, color=colors[i], label=f"Iterasi ke-{i}")

    plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label="Control Points")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()