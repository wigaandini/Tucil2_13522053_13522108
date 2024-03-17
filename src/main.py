from bezier import *
from input import *

print()
print("                         Welcome to Bézier Curve Generator!                                 \n")
print("██████╗ ███████╗███████╗██╗███████╗██████╗      ██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗")
print("██╔══██╗██╔════╝╚══███╔╝██║██╔════╝██╔══██╗    ██╔════╝██║   ██║██╔══██╗██║   ██║██╔════╝")
print("██████╔╝█████╗    ███╔╝ ██║█████╗  ██████╔╝    ██║     ██║   ██║██████╔╝██║   ██║█████╗")
print("██╔══██╗██╔══╝   ███╔╝  ██║██╔══╝  ██╔══██╗    ██║     ██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝")
print("██████╔╝███████╗███████╗██║███████╗██║  ██║    ╚██████╗╚██████╔╝██║  ██║ ╚████╔╝ ███████╗")
print("╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝\n")
print("     This program is used to create Bézier Curve using divide and conquer algorithm.")
print("--------------------------------------------------------------------------------------------")
print("                                 Wiga   -   Neo")
print("                               13522053 - 13522108")
print("--------------------------------------------------------------------------------------------\n")

while True:
    print("Choose algorithm to use ")
    print("1. Brute Force")
    print("2. Divide and Conquer")
    choice = input("Choice: ")
    if choice.isdigit():
        choice = int(choice)
        if choice in [1, 2]:
            break
    print("Invalid input. Please input 1 or 2.\n")

points = input_points()
i, t = input_iteration_and_t(choice)

if choice == 1:
    # bruteforce
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, False)
    print("Execution Time:", waktu_eksekusi, "ms")
    if (i <= 10) :
        print("Final Points Bézier Curve", titik_kurva)
    else :
        print("Total Points Bézier Curve:", len(titik_kurva), "points")
    show_kurva_bezier(points, i, t, False)
else :
    # dnc
    titik_kurva, waktu_eksekusi = kurva_bezier(points, i, t, True)
    print("Execution Time:", waktu_eksekusi, "ms")
    if (i <= 10) :
        print("Final Points Bézier Curve", titik_kurva)
    else :
        print("Total Points Bézier Curve:", len(titik_kurva), "points")
    show_kurva_bezier(points, i, t, True)