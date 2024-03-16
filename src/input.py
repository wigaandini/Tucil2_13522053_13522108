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
