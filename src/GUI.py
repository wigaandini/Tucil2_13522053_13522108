import tkinter as tk
from tkinter import messagebox
from bezier import *

def create_input(frame, label, row, column):
    label = tk.Label(frame, text=label)
    label.grid(row=row, column=column, padx=5, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=row, column=column+1)
    return entry

def generate_bezier_curve():
    try:
        n = int(entry_points.get())
        points = []
        for i in range(n):
            points.append(tuple(map(float, input_points[i].get().split())))
        iterations = int(entry_iterations.get())

        show_kurva_bezier(points, iterations, t=0.5, dnc=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Bézier Curve Generator")

label_title = tk.Label(root, text="Bézier Curve Generator", font=("Arial", 20), pady=20, padx=20) 
label_title.pack()

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_points = tk.Label(frame, text="Number of points (minimum 2):")
label_points.grid(row=0, column=0)
entry_points = tk.Entry(frame)
entry_points.grid(row=0, column=1)

input_points = []

def create_entry_points():
    num_points = int(entry_points.get())
    for widget in input_points:
        widget.destroy()
    input_points.clear()
    for i in range(num_points):
        if i == 0:
            entry = create_input(frame, "Start Point:", i+1, 0)
        elif i == num_points - 1:
            entry = create_input(frame, "Final Point:", i+1, 0)
        else:
            entry = create_input(frame, f"Control Point {i}:", i+1, 0)
        input_points.append(entry)

entry_points.bind("<FocusOut>", lambda event: create_entry_points())

entry_iterations = create_input(frame, "Number of Iteration:", 7, 0)

show_button = tk.Button(frame, text="Show the Bézier Curve", command=generate_bezier_curve)
show_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()